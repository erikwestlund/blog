from flask import Blueprint

from pages.views.admin import Index, FetchAdminPages
from pages.views.create import CreatePage
from pages.views.edit import EditPage, FetchPage
from pages.views.revisions import Revisions
from pages.views.show import ShowPage

pages = Blueprint("pages", __name__, template_folder="templates")


pages.add_url_rule(
    "/admin/pages/<int:page_id>.json", view_func=FetchPage.as_view("fetch_page")
)

pages.add_url_rule("/admin/pages", view_func=Index.as_view("fetch_admin_page"))
pages.add_url_rule("/admin/pages/create", view_func=CreatePage.as_view("create_page"))

pages.add_url_rule(
    "/admin/pages/<int:page_id>", view_func=EditPage.as_view("edit_page")
)

pages.add_url_rule(
    "/admin/pages.json", view_func=FetchAdminPages.as_view("fetch_admin_pages")
)
pages.add_url_rule("/<path:slug>", view_func=ShowPage.as_view("page"))


pages.add_url_rule(
    "/admin/pages/<int:page_id>/revisions", view_func=Revisions.as_view("revisions")
)
