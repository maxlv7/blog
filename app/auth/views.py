from flask import render_template,url_for,flash,request,redirect
from flask_login import login_required,login_user,logout_user,current_user
from . import auth
from .. import db
from ..models import User
from .forms import LoginForm,RegistrationForm
from ..decorators import admin_required


# 登录和注册
@auth.route('/log',methods=["GET","POST"])
@auth.route('/',methods=["GET","POST"])
def index():

    if current_user.is_authenticated:
        return redirect(url_for("main.index"))

    form_login = LoginForm()
    form_register = RegistrationForm()

    if form_login.submit_log.data and form_login.validate():
        user_login = User.query.filter_by(email=form_login.email.data).first()

        if user_login is not None and user_login.password == form_login.password.data:
            login_user(user_login)
            return redirect(url_for("main.index"))
        else:
            flash("邮箱或者密码错误!")

    if form_register.submit_reg.data and form_register.validate():
        user = User(name=form_register.username.data,email=form_register.email.data,password=form_register.password.data)
        db.session.add(user)
        db.session.commit()
        flash("成功注册，请登录！")
        return redirect(url_for("auth.index"))

    return render_template("sign in and up.html",login=form_login,reg=form_register)


@auth.route('/logout',methods=["GET"])
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))



# 测试login_required

# @auth.route('/tests')
# @login_required
# def test1():
#     return "success!"

# 测试admin_required

# @auth.route('/test_admin')
# @login_required
# @admin_required
# def is_admin():
#     return "ok"