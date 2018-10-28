# from app import db
from flask_script import Command
# from flask import Flask, current_app
# from app.users.models.user import User
# from flask import current_app



@with_appcontext
class InitialSeed(Command):

    admin_username = flask.current_app.config['ADMIN_INIT_USERNAME']
    admin_password = flask.current_app.config['ADMIN_INIT_PASSWORD']
    admin_email = flask.current_app.config['ADMIN_INIT_EMAIL']

    def run(self):
        print(self.admin_username)
    # admin_user = User(username=admin_username, password=admin_password,
        #              email=admin_email)
        # db.session.add(admin_user)
        # db.session.commit()