from flask import Blueprint

from main.views.index import Index
from main.views.admin import Admin
from main.views.tags import Tags

main = Blueprint("main", __name__, template_folder="templates", static_folder="static")

main.add_url_rule("/", view_func=Index.as_view("index"))
main.add_url_rule("/admin", view_func=Admin.as_view("admin"))

main.add_url_rule("/tags", view_func=Tags.as_view("tags"))
