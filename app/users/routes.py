from users.views.confirm_email import ConfirmEmail
from users.views.login import Login
from users.views.logout import Logout
from users.views.reset_password import ResetPassword
from users.views.register import Register
from flask import Blueprint

users = Blueprint('users', __name__, template_folder='templates')

users.add_url_rule('/login', view_func=Login.as_view('login'))
users.add_url_rule('/logout', view_func=Logout.as_view('logout'))
users.add_url_rule('/register', view_func=Register.as_view('register'))
users.add_url_rule('/users/reset-password',
                   view_func=ResetPassword.as_view('reset_password'))
users.add_url_rule('/users/confirm-email/<token>',
                   view_func=ConfirmEmail.as_view('confirm_email'))
