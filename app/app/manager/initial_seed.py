from app import db
from flask_script import Command
# from app.users.models.user import User
# from flask import current_app

class InitialSeed(Command):
    # admin_username = current_app.config['ADMIN_USERNAME']
    # admin_password = current_app.config['ADMIN_PASSWORD']
    # admin_email = current_app.config['ADMIN_EMAIL']

    def run(self):
        print('test')
        # admin_user = User(username=admin_username, password=admin_password,
        #              email=admin_email)
        # db.session.add(admin_user)
        # db.session.commit()