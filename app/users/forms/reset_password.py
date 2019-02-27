from flask_wtf import FlaskForm
from wtforms import PasswordField
from wtforms.validators import DataRequired, EqualTo


class ResetPasswordForm(FlaskForm):
    password = PasswordField("Password", validators=[DataRequired()])
    password_confirm = PasswordField(
        "Confirm Password", validators=[DataRequired(), EqualTo("password")]
    )
