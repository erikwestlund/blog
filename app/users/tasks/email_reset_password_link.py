from app import celery
from app import mail
from users.models.user import User
from flask import current_app
from flask import render_template, url_for
from flask_mail import Message


@celery.task()
def email_reset_password_link(user_id):
    user = User.query.get(user_id)
    token = user.generate_password_reset_token()

    msg = Message((current_app.config['BLOG_TITLE'] or 'Blog') + ': Password Reset Request',
                  recipients=[user.email])
    msg.html = render_template('users/reset_password_email.html',
                               reset_password_url=url_for('users.reset_password', token=token))
    mail.send(msg)