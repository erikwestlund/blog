from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Optional

from utils.forms.nonvalidatingmultiselectfield import NonValidatingMultiSelectField


class SavePostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])

    body = StringField("Body", validators=[DataRequired()])

    tags = NonValidatingMultiSelectField("Tags", choices=[])

    published_at = StringField("Published At", validators=[Optional()])
