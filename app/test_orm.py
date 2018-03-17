from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask import Flask
import random


app = Flask(__name__)

app.config.update(
    DEBUG = True,
    SQLALCHEMY_DATABASE_URI = "mysql://root:root@localhost:3306/dev_blog",
    SQLALCHEMY_TRACK_MODIFICATIONS = True
)

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64),unique=True)
    email = db.Column(db.String(64),unique=True)
    password = db.Column(db.String(128))
    admin = db.Column(db.Boolean,default=False)
    creat_at = db.Column(db.DateTime,default=datetime.utcnow())


class Blog(db.Model):
    __tablename__ = "blogs"

    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer)
    user_name = db.Column(db.String(64))
    name = db.Column(db.String(64))
    summary = db.Column(db.Text)
    content = db.Column(db.Text)
    create_at = db.Column(db.DateTime,default=datetime.utcnow())

class Comments(db.Model):
    id = db.Column(db.Integer,primary_key=True,unique=True)
    user_id = db.Column(db.Integer)
    user_name = db.Column(db.String(64))
    email = db.Column(db.String(64))
    content = db.Column(db.Text)
    create_at = db.Column(db.DateTime,default=datetime.now())

db.init_app(app)

with app.app_context():
    # db.drop_all()
    db.create_all()

@app.route("/",methods=["GET"])
def index():
    # u1 = User(id=1,name="li",email="admin@maxlv.org",password="123213")
    # u = User(id=2,name="li2",email="admin1@maxlv.org",password="123213")

    blog = Blog(id=1,user_id=2,user_name="123",summary="123123123",content="alsghlaghlka")
    db.session.add(blog)
    db.session.commit()
    return "K!"
if __name__ == '__main__':

    app.run(port=9000)