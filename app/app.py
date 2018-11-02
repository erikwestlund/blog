from flask import Flask
from flask_bcrypt import Bcrypt
from flask_debugtoolbar import DebugToolbarExtension
from flask_login import LoginManager
from flask_mail import Mail
from flask_migrate import Migrate
from flask_redis import FlaskRedis
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

from app_state import app_state
from celery_context import FlaskCelery
from config import Config
from utils.session import RedisSessionInterface

db = SQLAlchemy()
celery = FlaskCelery()
redis = FlaskRedis()
mail = Mail()
migrate = Migrate()
bcrypt = Bcrypt()
csrf = CSRFProtect()

login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'warning'
login_manager.refresh_view = 'users.login'
login_manager.needs_refresh_message_category = 'warning'


def init_extensions(app):
    db.init_app(app)
    celery.init_app(app)
    redis.init_app(app)
    mail.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)


def init_session(app):
    prefix = app.config['REDIS_SESSION_PREFIX']
    app.session_interface = RedisSessionInterface(redis=redis, prefix=prefix)


def init_blueprints(app):
    from main.routes import main
    from users.routes import users
    from posts.routes import posts

    app.register_blueprint(main)
    app.register_blueprint(users)
    app.register_blueprint(posts)

    from utils.filters import filters

    app.register_blueprint(filters)


def init_state(app):
    @app.context_processor
    def context_processor():
        return app_state()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    DebugToolbarExtension(app)

    init_extensions(app)
    init_session(app)
    init_blueprints(app)
    init_state(app)

    return app