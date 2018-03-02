from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
from datetime import datetime

'''
各种包的初始化
'''

db = SQLAlchemy()

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

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    # config[config_name].init_app(app)
    # print(config[config_name].SQLALCHEMY_DATABASE_URL)

    # 初始化数据表
    db.init_app(app)

    with app.app_context():
        db.drop_all()
        db.create_all()

    from .main import main as main_route

    app.register_blueprint(main_route)

    return app


# print(config["development"].SQLALCHEMY_DATABASE_URL)

