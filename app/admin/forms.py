from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,IntegerField,TextAreaField
from wtforms.validators import Required,EqualTo
from flask_pagedown.fields import PageDownField

class BlogForm(FlaskForm):
    user_id = IntegerField()
    user_name = StringField()
    name = StringField("标题",validators=[Required()])
    summary = TextAreaField("摘要",validators=[Required()])
    content = PageDownField("内容",validators=[Required()])
    submit = SubmitField("发表文章")