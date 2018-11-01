from flask import Blueprint, render_template, redirect
from app.main.views.index import Index

main = Blueprint('main', __name__, template_folder='templates', static_folder='static')

main.add_url_rule('/', view_func=Index.as_view('index'))
