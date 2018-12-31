from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class SavePostForm(FlaskForm):
    subject = StringField('Subject',
                           validators=[DataRequired()])
    body = StringField('Body',
                       validators=[DataRequired()])
