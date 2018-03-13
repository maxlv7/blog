# 定义数据表的原型
from datetime import datetime
from flask_login import UserMixin,AnonymousUserMixin
from . import db,login_manager
import bleach
from markdown import markdown


class User(UserMixin,db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64),unique=True)
    email = db.Column(db.String(64),unique=True)
    password = db.Column(db.String(128))
    admin = db.Column(db.Boolean,default=False)
    creat_at = db.Column(db.DateTime,default=datetime.utcnow())

    def __init__(self,**kwargs):
        super().__init__(**kwargs)

    def is_administrator(self):
        return self.admin

    @staticmethod
    def create_admin():
        u = User(email = '123@123.com',
                 name = '123',
                 password = '123',
                 admin = True)
        db.session.add(u)
        db.session.commit()


class Blog(db.Model):
    __tablename__ = "blogs"

    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer)
    user_name = db.Column(db.String(64))
    name = db.Column(db.String(64))
    summary = db.Column(db.Text)
    content = db.Column(db.Text)
    content_html = db.Column(db.Text)
    create_at = db.Column(db.DateTime,default=datetime.utcnow())


    @staticmethod
    def on_change_content(target,value,oldvalue,initiator):
        allow_tags = [
            'a','abbr','acronym','b','blockquote','code','em','i','li','ol','pre','strong','ul',
            'h1','h2','h3','p'
        ]
        # exts = ['markdown.extensions.extra', 'markdown.extensions.codehilite', 'markdown.extensions.tables',
        #         'markdown.extensions.toc']
        target.content_html = bleach.linkify(bleach.clean(markdown(value,output_format='html'),tags=allow_tags,strip=True))

db.event.listen(Blog.content,'set',Blog.on_change_content)


# 加载用户的回调函数
@login_manager.user_loader
def load_user(user_id):
    # s = User.query.get(user_id)
    return User.query.get(user_id)


class Anonymous_myUser(AnonymousUserMixin):
    def is_administrator(self):
        return False

# 创建匿名用户的回调
login_manager.anonymous_user = Anonymous_myUser




