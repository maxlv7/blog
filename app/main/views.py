from flask import render_template,url_for,redirect,request
from flask_login import current_user
from ..models import Blog,Comment,db
from . import main
from .form import CommentsForm

@main.route('/',methods=["GET"])
@main.route('/index',methods=['GET'])
def index():

    length = len(Blog.query.all())
    new_blogs = Blog.query.order_by(Blog.id)
    l = list()
    l.append(new_blogs[length-1])
    l.append(new_blogs[length-2])

    # return "ok"
    return render_template("index.html",blogs=l)

@main.route('/about',methods=['GET'])
def about():

    return render_template("about.html")

@main.route('/contact',methods=['GET'])
def contact():

    return render_template("contact.html")

@main.route('/content/<int:id>',methods=['GET','POST'])
def blog_content(id):
    comment = CommentsForm()

    # 查询数据
    comments = Comment.query.filter_by(blog_id=id).all()


    # 表单提交
    if comment.submit.data and comment.validate():
        comment = Comment(
            user_id=current_user.id,
            blog_id = id,
            user_name=comment.user_name.data,
            label=comment.label.data,
            email=comment.email.data,
            content=comment.content.data
        )
        db.session.add(comment)
        db.session.commit()

        return redirect(url_for("main.blog_content",id=id))


    blog = Blog.query.filter_by(id=id).first_or_404()
    return render_template("content.html",blog=blog,comment=comment,comm=comments)

@main.route('/links',methods=['GET'])
def links():

    return render_template("links.html")

@main.route('/blogs',methods=['GET'])
def blogs():

    blogs = Blog.query.all()

    return render_template("blogs.html",blogs=blogs)