from flask_script import Command
import flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
import datetime

class InitialSeed(Command):

    def run(self):
        bcrypt = Bcrypt(flask.current_app)
        db = SQLAlchemy(flask.current_app)

        # seed roles
        from app.users.models.user import Role

        admin_role = Role(name="administrator",
                          description="Can administrate site")
        db.session.add(admin_role)

        user_role = Role(name="user",
                          description="Basic user")
        db.session.add(user_role)

        #seed user
        admin_username = flask.current_app.config['ADMIN_INIT_USERNAME']
        admin_password = flask.current_app.config['ADMIN_INIT_PASSWORD']
        admin_password_hashed = bcrypt.generate_password_hash(admin_password).decode('utf-8')
        admin_email = flask.current_app.config['ADMIN_INIT_EMAIL']

        from app.users.models.user import User
        admin_user = User(username=admin_username,
                          password=admin_password_hashed,
                          email=admin_email,
                          email_confirmed_at=datetime.datetime.now())

        admin_user.roles.append(admin_role)

        db.session.add(admin_user)
        db.session.commit()