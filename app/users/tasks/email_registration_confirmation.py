from app import celery
from app import mail
from users.models.user import User
from flask import current_app
from flask import render_template, url_for
from flask_mail import Message


@celery.task()
def email_registration_confirmation(user_id):
    user = User.query.get(user_id)
    token = user.generate_confirmation_token()

    msg = Message((current_app.config['BLOG_TITLE'] or 'Blog') + ': Email Registration Confirmation',
                  recipients=[user.email])
    msg.html = render_template('users/confirm_email.html',
                               confirm_url=url_for('users.confirm_email', token=token))
    mail.send(msg)
