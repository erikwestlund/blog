from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FieldList
from wtforms.validators import DataRequired, Optional
from utils.forms.nonvalidatingselectfield import NonValidatingSelectField


class SavePostForm(FlaskForm):
    action = StringField('Action',
                           validators=[DataRequired()])

    post_id = IntegerField('Post ID',
                           validators=[Optional()])

    title = StringField('Title',
                           validators=[DataRequired()])
    body = StringField('Body',
                       validators=[DataRequired()])

    tags = NonValidatingSelectField('Tags', choices=[]
                                    )
