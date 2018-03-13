from flask import render_template,url_for,redirect
from ..models import Blog
from . import main

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

@main.route('/content/<int:id>',methods=['GET'])
def blog_content(id):

    blog = Blog.query.filter_by(id=id).first_or_404()
    return render_template("content.html",blog=blog)

@main.route('/links',methods=['GET'])
def links():

    return render_template("links.html")

@main.route('/blogs',methods=['GET'])
def blogs():

    blogs = Blog.query.all()

    return render_template("blogs.html",blogs=blogs)