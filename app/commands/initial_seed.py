import datetime

import flask
from flask_bcrypt import Bcrypt
from flask_script import Command
from flask_sqlalchemy import SQLAlchemy


class InitialSeed(Command):

    def run(self):
        prod = input('Is this a production seed? [yes/no]' + "\n")

        if str(prod).lower() == 'yes' and not self.check_safe():
            return

        bcrypt = Bcrypt(flask.current_app)
        db = SQLAlchemy(flask.current_app)

        # seed roles
        from users.models.role import Role

        admin_role = Role(name="administrator",
                          display_name="Administrator",
                          description="Can administrate site")
        db.session.add(admin_role)

        writer_role = Role(name="writer",
                          display_name="Writer",
                          description="Can write posts for site")
        db.session.add(writer_role)

        user_role = Role(name="user",
                         display_name="User",
                         description="Basic user")
        db.session.add(user_role)

        # seed user
        admin_username = flask.current_app.config['ADMIN_INIT_USERNAME']
        admin_password = flask.current_app.config['ADMIN_INIT_PASSWORD']
        admin_password_hashed = bcrypt.generate_password_hash(admin_password).decode('utf-8')
        admin_email = flask.current_app.config['ADMIN_INIT_EMAIL']

        from users.models.user import User
        admin_user = User(username=admin_username,
                          password=admin_password_hashed,
                          email=admin_email,
                          active=True,
                          email_confirmed_at=datetime.datetime.now())

        admin_user.roles.append(admin_role)
        admin_user.roles.append(writer_role)

        db.session.add(admin_user)
        db.session.commit()

    def check_safe(self):
        admin_password = flask.current_app.config['ADMIN_INIT_PASSWORD']
        secret_key = flask.current_app.config['SECRET_KEY']

        if not admin_password:
            print("Please enter a password for the administrator user in your .env file.")
            return False
        elif admin_password == 'password':
            print('Please change the admin password in your .env file.')
            return False
        elif secret_key == 'supersecretkey':
            print('Please set the secret key in your .env to something secure.')
            return False

        return True