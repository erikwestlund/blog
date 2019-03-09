from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import (
    DataRequired,
    Length,
    Email,
    EqualTo,
    ValidationError,
    Optional,
)

from users.models.user import User
from utils.forms.multicheckboxfield import MultiCheckboxField


class UpdateAccountForm(FlaskForm):
    def __init__(self, user_being_edited):
        super(UpdateAccountForm, self).__init__()
        self.user_being_edited = user_being_edited

    username = StringField(
        "Username", validators=[DataRequired(), Length(min=2, max=20)]
    )
    email = StringField("Email", validators=[DataRequired(), Email()])
    first_name = StringField()
    last_name = StringField()
    password = PasswordField("Password", validators=[Optional(), Length(min=6)])
    password_confirm = PasswordField(
        "Confirm Password", validators=[EqualTo("password")]
    )
    user_roles = MultiCheckboxField(choices=["1", "2", "3"])

    def validate_username(self, username):
        if self.user_being_edited.username != username.data:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError(
                    "That username is taken. Please choose a different one."
                )

    def validate_email(self, email):
        if self.user_being_edited.email != email.data:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError(
                    "That email is taken. Please choose a different one."
                )
