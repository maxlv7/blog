import os

'''程序的配置文件'''

# 程序的绝对文件位置
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRT_KEY = os.environ.get("SECRT_KEY") or "kang"
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    @staticmethod
    def init_app(app):
        pass

# 基类 Config 中包含通用配置，子类分别定义专用的配置。如果需要，你还可添加其他配置类。
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URL = os.environ.get("DEV_DATABASE_URL") or "mysql://root:root@localhost:3306/test"

class ProductionConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URL = os.environ.get("DEV_DATABASE_URL") or "mysql://root:root@localhost:3306/test"

config = {
    "development":DevelopmentConfig,
    "production":ProductionConfig
}

if __name__ == '__main__':

    print(config["development"].SQLALCHEMY_DATABASE_URL)