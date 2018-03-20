from flask import render_template,redirect,url_for,flash
from . import admin
from .forms import BlogForm
from ..models import Blog,User,Comment
from .. import db
from ..decorators import admin_required
from flask_login import login_required,current_user


@admin.route('/index')
@admin.route('/')
@login_required
@admin_required
def index():
    blog_counts = len(Blog.query.all())
    comment_counts = len(Comment.query.all())
    return render_template("admin_index.html",blog_counts=blog_counts,comment_counts=comment_counts)


# 创建文章
@admin.route('/create_blog',methods=["GET","POST"])
@login_required
@admin_required
def create_blog():
    form = BlogForm()

    if form.submit.data and form.validate():
        blog = Blog(
            user_id = current_user.id,
            user_name = current_user.name,
            name = form.name.data,
            summary = form.summary.data,
            content=form.content.data
        )
        db.session.add(blog)
        db.session.commit()
        flash("发表成功！")
        return redirect(url_for("admin.create_blog"))

    return render_template("admin_create_blog.html",form=form)


# 管理用户
@admin.route('/manage_users',methods=["GET","POST"])
@login_required
@admin_required
def manage_users():

    users = User.query.all()


    return render_template("admin_manage_users.html",users=users)



# 删除用户
@admin.route('/del_user/<int:id>',methods=["GET","POST"])
@login_required
@admin_required
def del_user(id):

    user = User.query.filter_by(id=id).first_or_404()

    db.session.delete(user)

    db.session.commit()

    return redirect(url_for("admin.manage_users"))


# 管理文章
@admin.route('/manage_blogs',methods=["GET","POST"])
@login_required
@admin_required
def manage_blogs():

    blogs = Blog.query.all()

    return render_template("admin_manage_blogs.html",blogs=blogs)

# 删除文章
@admin.route('/del_blog/<int:id>',methods=["GET","POST"])
@login_required
@admin_required
def del_blog(id):

    blog = Blog.query.filter_by(id=id).first_or_404()

    db.session.delete(blog)

    db.session.commit()

    return redirect(url_for("admin.manage_blogs"))

# 管理评论
@admin.route('/manage_comments')
@login_required
@admin_required
def manage_comments():

    comments = Comment.query.all()

    return render_template("admin_manage_comments.html",comments=comments)

# 删除评论
@admin.route('/del_comment/<int:id>',methods=["GET","POST"])
@login_required
@admin_required
def del_comment(id):

    comment = Comment.query.filter_by(id=id).first_or_404()

    db.session.delete(comment)

    db.session.commit()

    return redirect(url_for("admin.manage_comments"))

# 设置管理员
@admin.route('/set_admin_user/<int:id>',methods=["GET","POST"])
@login_required
@admin_required
def set_admin_user(id):

    user = User.query.filter_by(id=id).first_or_404()

    user.admin = 1

    db.session.commit()

    return redirect(url_for("admin.manage_users"))
