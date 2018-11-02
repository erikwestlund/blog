from flask import Blueprint

from blog.views.index import Index

blog = Blueprint('blog', __name__, template_folder='templates', static_folder='static')

blog.add_url_rule('/', view_func=Index.as_view('index'))
