from flask_wtf import FlaskForm
from wtforms import StringField, DateTimeField
from wtforms.validators import DataRequired, Optional, ValidationError

from utils.forms.nonvalidatingmultiselectfield import NonValidatingMultiSelectField
from posts.models.post import Post


class SavePostForm(FlaskForm):
    def __init__(self, post_being_edited=None):
        super(SavePostForm, self).__init__()
        self.post_being_edited = post_being_edited

    title = StringField("Title", validators=[DataRequired()])

    body = StringField("Body", validators=[DataRequired()])

    uploaded_images = NonValidatingMultiSelectField("Images", choices=[])

    tags = NonValidatingMultiSelectField("Tags", choices=[])

    published_at = StringField("Published At", validators=[Optional()])

    slug = StringField("slug", validators=[Optional()])

    def validate_slug(self, slug):
        if self.post_being_edited and self.post_being_edited.slug != slug.data:
            if Post.slug_exists_within_month(slug.data, self.published_at.data):
                raise ValidationError(
                    "That slug is taken for this month. Please enter a different one."
                )
