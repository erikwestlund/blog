from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Optional, ValidationError

from utils.forms.nonvalidatingmultiselectfield import NonValidatingMultiSelectField
from pages.models.page import Page


class SavePageForm(FlaskForm):
    def __init__(self, page_being_edited=None):
        super(SavePageForm, self).__init__()
        self.page_being_edited = page_being_edited

    title = StringField("Title", validators=[DataRequired()])

    body = StringField("Body", validators=[DataRequired()])

    uploaded_images = NonValidatingMultiSelectField("Images", choices=[])

    primary_image_id = StringField("Primary Image Id", validators=[Optional()])

    slug = StringField("slug", validators=[Optional()])

    def validate_slug(self, slug):
        if self.page_being_edited and self.page_being_edited.slug != slug.data:
            if Page.slug_exists_within_month(slug.data, self.published_at.data):
                raise ValidationError(
                    "That slug is taken for this month. Please enter a different one."
                )
