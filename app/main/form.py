from flask_wtf import FlaskForm
from wtforms.validators import DataRequired,Email
from wtforms.fields import StringField,SubmitField,IntegerField,TextAreaField

class CommentsForm(FlaskForm):
    user_id = IntegerField()
    user_name = StringField(validators=[DataRequired()])
    label = StringField()
    email = StringField(validators=[DataRequired(),Email()])
    content = TextAreaField(validators=[DataRequired()])
    submit = SubmitField()


