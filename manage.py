from app import create_app,db
from app.models import User,Blog
"""用于启动程序和其它的程序任务"""

manange = create_app("development")


manange.run()