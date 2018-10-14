from flask import Flask
from flaskext.versioned import Versioned

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
versioned = Versioned(app)

from blog import routes

