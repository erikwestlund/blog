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

    slug = StringField("Slug", validators=[DataRequired()])

    body = StringField("Body", validators=[DataRequired()])

    uploaded_images = NonValidatingMultiSelectField("Images", choices=[])

    primary_image_id = StringField("Primary Image Id", validators=[Optional()])


    def validate_slug(self, slug):
        if self.page_being_edited and self.page_being_edited.slug != slug.data:
            if Page.query.filter_by(slug=slug.data).count() > 0:
                raise ValidationError(
                    "That slug is taken. Please enter a different one."
                )

            if self.slug in ["users", "admin", "contact", "posts", "pages"]:
                raise ValidationError(
                    "That slug is reserved."
                )