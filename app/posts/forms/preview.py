from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class PreviewForm(FlaskForm):
    body = StringField("Body", validators=[DataRequired()])
