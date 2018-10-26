from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from app.config import Config
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_debugtoolbar import DebugToolbarExtension
from flask_login import current_user

db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
csrf = CSRFProtect()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'


def load_models():
    from app.users.models.user import User


load_models()


def init_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)


def init_blueprints(app):
    from app.main.views import main
    from app.users.views import users
    from app.posts.views import posts
    from app.utils.filters import utils

    app.register_blueprint(main)
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(utils)


def init_state(app):
    @app.context_processor
    def inject_state():
        return dict(
            state={
                'user': {
                    'logged_in': current_user.is_authenticated
                }
            }
        )


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    toolbar = DebugToolbarExtension(app)

    init_extensions(app)
    init_blueprints(app)

    init_state(app)

    return app


manager = Manager(create_app)

manager.add_command('db', MigrateCommand)

