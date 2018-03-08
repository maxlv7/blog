# 定义数据表的原型
from datetime import datetime
from flask_login import UserMixin
from . import db,login_manager


class User(UserMixin,db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64),unique=True)
    email = db.Column(db.String(64),unique=True)
    password = db.Column(db.String(128))
    admin = db.Column(db.Boolean,default=False)
    creat_at = db.Column(db.DateTime,default=datetime.utcnow())


class Blog(db.Model):
    __tablename__ = "blogs"

    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer)
    user_name = db.Column(db.String(64))
    name = db.Column(db.String(64))
    summary = db.Column(db.Text)
    content = db.Column(db.Text)
    create_at = db.Column(db.DateTime,default=datetime.utcnow())

# 加载用户的回调函数
@login_manager.user_loader
def load_user(user_id):
    # s = User.query.get(user_id)
    return User.query.get(user_id)

