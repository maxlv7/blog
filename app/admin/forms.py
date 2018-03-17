from flask_wtf import FlaskForm
from wtforms.fields import StringField,SubmitField,IntegerField,TextAreaField
from wtforms.validators import DataRequired,EqualTo
from flask_pagedown.fields import PageDownField

class BlogForm(FlaskForm):
    user_id = IntegerField()
    user_name = StringField()
    name = StringField("标题",validators=[DataRequired()])
    summary = TextAreaField("摘要",validators=[DataRequired()])
    content = PageDownField("内容",validators=[DataRequired()])
    submit = SubmitField("发表文章")