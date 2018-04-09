from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import config
from flask_pagedown import PageDown

'''
各种包的初始化
'''

login_manager = LoginManager()
login_manager.session_protection = "basic"
login_manager.login_view = "auth.index"
login_manager.login_message = "请登录后访问！"
db = SQLAlchemy()
pagedown = PageDown()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    # config[config_name].init_app(app)
    # print(config[config_name].SQLALCHEMY_DATABASE_URL)
    # 初始化数据表
    db.init_app(app)

    # 初始化flask_login
    login_manager.init_app(app)

    #初始化flask_pagedown
    pagedown.init_app(app)

    # 注册蓝图


    from .API import API as api_route

    app.register_blueprint(api_route)


    from .auth import auth as auth_route

    app.register_blueprint(auth_route)

    from .main import main as main_route

    app.register_blueprint(main_route)

    from .admin import admin as admin_route

    app.register_blueprint(admin_route)

    return app


# print(config["development"].SQLALCHEMY_DATABASE_URL)

