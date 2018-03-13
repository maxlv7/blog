from flask import render_template,jsonify
from . import API
from .. import db
from ..models import User,Blog

# 获取所有用户
@API.route('/users/all_users',methods=['GET'])
def get_all_user():
    user = User.query.filter_by(id=1).one()

    # return user["name"]+" " + user["create_at"]
    return jsonify(id=user.id,name=user.name,create_at=user.creat_at,admin=user.admin,password=user.password)

#获取单个用户的信息
@API.route('/users/user_profiles/id=<int:id>',methods=["GET"])
def get_user_profiles_by_id(id):
    user = User.query.filter_by(id=id).one()
    user.password = "******"
    return jsonify(id=user.id,name=user.name,create_at=user.creat_at,admin=user.admin,password=user.password)


#获取单篇博客
@API.route('/blog/<int:id>',methods=["GET"])
def get_single_blog_by_id(id):
    blog = Blog.query.filter_by().one()
    return None

@API.route('/creat_admin')
def create_admin():
    User.create_admin()
    return "ok"

