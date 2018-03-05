from app import create_app
"""用于启动程序和其它的程序任务"""

manage = create_app("development")

if __name__ == '__main__':

    manage.run()