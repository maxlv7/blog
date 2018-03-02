from app import create_app

"""用于启动程序和其它的程序任务"""

manange = create_app("development")
manange.run()