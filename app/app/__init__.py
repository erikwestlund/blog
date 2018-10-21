from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flaskext.versioned import Versioned
from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect()

app = Flask(__name__)

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
csrf.init_app(app)

versioned = Versioned(app)

# blueprints
from app.users.views import users_blueprint

app.register_blueprint(users_blueprint)

# global views
from app import views