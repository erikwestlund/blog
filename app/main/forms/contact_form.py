from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Optional, ValidationError, Email

from utils.forms.nonvalidatingmultiselectfield import NonValidatingMultiSelectField
from posts.models.post import Post


class ContactForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    body = TextAreaField("Body", validators=[DataRequired()])
