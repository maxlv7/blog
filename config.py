import os

'''程序的配置文件'''

# 程序的绝对文件位置
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # SECRET_KEY = os.environ.get("SECRET_KEY") or "kang"
    SECRET_KEY = "hard to guess"
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True


    # 感觉不到作用在哪儿
    @staticmethod
    def init_app(app):
        # print("----init app----")
        pass


# 基类 Config 中包含通用配置，子类分别定义专用的配置。如果需要，你还可添加其他配置类。
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DEV_DATABASE_URL") or "mysql://root:root@localhost:3306/dev_blog"
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get("DEV_DATA  BASE_URL") or "mysql://root:root@localhost:3306/test"

config = {
    "development":DevelopmentConfig,
    "production":ProductionConfig
}

if __name__ == '__main__':

    print(config["development"].SQLALCHEMY_DATABASE_URL)