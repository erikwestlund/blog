from flask import render_template
from flask.views import MethodView

from pages.models.page import Page
from utils.models.find_or_fail import find_or_fail


class ShowPage(MethodView):
    def get(self, slug):
        page = find_or_fail(Page, Page.slug == slug)

        return render_template('pages/show.html', title=page.title, page=page)
