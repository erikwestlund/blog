from users.views.account import Account
from users.views.confirm_email import ConfirmEmail
from users.views.confirm_email_request import ConfirmEmailRequest
from users.views.login import Login
from users.views.logout import Logout
from users.views.reset_password import ResetPassword
from users.views.reset_password_request import ResetPasswordRequest
from users.views.register import Register
from users.views.admin import AdminUsersIndex, AdminUsersIndexJson
from flask import Blueprint

users = Blueprint('users', __name__, template_folder='templates')

users.add_url_rule('/account', view_func=Account.as_view('account'), methods=['GET'])
users.add_url_rule('/users/<int:user_id>/edit',
                   view_func=Account.as_view('edit_user'),
                   methods=['GET', 'POST'])

users.add_url_rule('/login', view_func=Login.as_view('login'))
users.add_url_rule('/logout', view_func=Logout.as_view('logout'))
users.add_url_rule('/register', view_func=Register.as_view('register'))
users.add_url_rule('/users/reset-password/<token>',
                   view_func=ResetPassword.as_view('reset_password'))
users.add_url_rule('/users/reset-password',
                   view_func=ResetPasswordRequest.as_view('reset_password_request'))
users.add_url_rule('/users/confirm-email/<token>',
                   view_func=ConfirmEmail.as_view('confirm_email'))
users.add_url_rule('/users/confirm-email',
                   view_func=ConfirmEmailRequest.as_view('confirm_email_request'))

users.add_url_rule('/admin/users', view_func=AdminUsersIndex.as_view('admin_users_index'))
users.add_url_rule('/admin/users.json', view_func=AdminUsersIndexJson.as_view('admin_users_index_json'))
