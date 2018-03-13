from flask import render_template
from . import admin
from .forms import BlogForm
from ..models import Blog
from .. import db
from ..decorators import admin_required
from flask_login import login_required


@admin.route('/index')
@admin.route('/')
@login_required
@admin_required
def index():
    blog_counts = len(Blog.query.all())
    return render_template("admin_index.html",blog_counts=blog_counts)

@login_required
@admin_required
@admin.route('/create_blog',methods=["GET","POST"])
def create_blog():
    form = BlogForm()

    if form.submit.data and form.validate:
        blog = Blog(
            name=form.name.data,
            summary = form.summary.data,
            content=form.content.data
        )
        db.session.add(blog)
        db.session.commit()

    return render_template("admin_create_blog.html",form=form)