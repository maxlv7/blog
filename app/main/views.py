from flask import render_template,url_for,redirect
from ..models import Blog
from . import main

@main.route('/index',methods=['GET'])
def index():
    return render_template("index.html")

@main.route('/about',methods=['GET'])
def about():
    return render_template("about.html")

@main.route('/contact',methods=['GET'])
def contact():
    return render_template("contact.html")

@main.route('/content',methods=['GET'])
def content():
    return render_template("content.html")

@main.route('/links',methods=['GET'])
def links():
    return render_template("links.html")

@main.route('/blogs',methods=['GET'])
def blogs():

    blogs = Blog.query.filter_by(id=1).all()

    return render_template("blogs.html",blogs=blogs)