from flask_wtf import FlaskForm
from wtforms.fields import StringField,PasswordField,SubmitField
from wtforms import ValidationError
from wtforms.validators import DataRequired,Length,Email,EqualTo
from ..models import User

# 登陆表单
class LoginForm(FlaskForm):
    email = StringField("邮箱",validators=[DataRequired(),Length(1,64),Email()])
    password = PasswordField("密码",validators=[DataRequired()])
    submit_log = SubmitField("登录")

# 注册表单
class RegistrationForm(FlaskForm):
    email = StringField('电子邮箱', validators=[DataRequired(), Length(1, 64),
                                                Email()])
    username = StringField('你的昵称', validators=[DataRequired(), Length(1, 64)])
    password = PasswordField('输入密码', validators=[
        DataRequired(), EqualTo('password2', message='两次输入密码不一致')])
    password2 = PasswordField('确认密码', validators=[DataRequired()])
    submit_reg = SubmitField('注册')

