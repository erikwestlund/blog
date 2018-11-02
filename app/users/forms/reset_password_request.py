from flask_wtf import FlaskForm
from wtforms import StringField, ValidationError
from wtforms.validators import DataRequired, Email

from users.models.user import User


class ResetPasswordRequestForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('Provided email address does not match out records.')