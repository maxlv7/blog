from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config

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

    # 注册蓝图


    from .API import API as api_route

    app.register_blueprint(api_route)


    from .auth import auth as auth_route

    app.register_blueprint(auth_route)

    from .main import main as main_route

    app.register_blueprint(main_route)

    return app


# print(config["development"].SQLALCHEMY_DATABASE_URL)

