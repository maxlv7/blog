from flask import Blueprint

"""创建蓝本"""

main = Blueprint('main',__name__,static_folder='../assets',template_folder='./templates')

from . import views

