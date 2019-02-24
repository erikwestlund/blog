from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Optional


class SavePostForm(FlaskForm):
    action = StringField('Action',
                           validators=[DataRequired()])

    post_id = IntegerField('Post ID',
                           validators=[Optional()])

    title = StringField('Title',
                           validators=[DataRequired()])
    body = StringField('Body',
                       validators=[DataRequired()])
