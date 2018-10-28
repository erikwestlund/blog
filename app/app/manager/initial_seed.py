from flask_script import Command
import flask


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