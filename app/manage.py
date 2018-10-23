from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    return app


app = create_app()

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()