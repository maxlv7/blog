# 定义数据表的原型
from datetime import datetime
from . import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(64),unique=True)
    email = db.Column(db.String(64),unique=True)
    password = db.Column(db.String(128))
    admin = db.Column(db.Boolean,default=False)
    creat_at = db.Column(db.DateTime,default=datetime.utcnow())

class Blog():
    __tablename__ = "blogs"

    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer)
    user_name = db.Column(db.String(64))
    name = db.Column(db.String(64))
    summary = db.Column(db.Text)
    content = db.Column(db.Text)

