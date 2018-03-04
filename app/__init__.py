from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
from datetime import datetime

'''
各种包的初始化
'''

db = SQLAlchemy()



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

