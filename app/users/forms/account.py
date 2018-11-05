from users.models.user import User
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Optional
from flask_login import current_user
from utils.forms.multicheckboxfield import MultiCheckboxField
from users.models.role import Role
from funcy import lpluck_attr


class UpdateAccountForm(FlaskForm):

    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    first_name = StringField()
    last_name = StringField()
    password = PasswordField('Password', validators=[Optional(), Length(min=6)])
    password_confirm = PasswordField('Confirm Password',
                                     validators=[EqualTo('password')])
    user_roles = MultiCheckboxField(choices=['1', '2'])

    def validate_username(self, username):
        if current_user.username != username.data:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        if current_user.email != email.data:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')
