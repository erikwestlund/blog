from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from app.config import Config
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_debugtoolbar import DebugToolbarExtension
import json

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
    from app.main.views import main_blueprint
    from app.users.views import users_blueprint
    from app.posts.views import posts_blueprint

    app.register_blueprint(main_blueprint)
    app.register_blueprint(users_blueprint)
    app.register_blueprint(posts_blueprint)


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    toolbar = DebugToolbarExtension(app)

    init_extensions(app)
    init_blueprints(app)

    return app

def get_asset_version(file):
    with open('mix-manifest.json') as f:
        data = json.load(f)

    return data['/' + file]

manager = Manager(create_app)

manager.add_command('db', MigrateCommand)
