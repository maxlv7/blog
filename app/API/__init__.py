from flask import Blueprint

API = Blueprint("api",__name__,url_prefix='/api')

from . import views