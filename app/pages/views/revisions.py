import json

from flask import jsonify, abort
from flask.views import MethodView

from pages.models.page import Page
from utils.acl import user_has_role
from utils.models.find_or_fail import find_or_fail


class Revisions(MethodView):
    @user_has_role("administrator")
    def get(self, page_id):
        page = find_or_fail(Page, Page.id == page_id)

        revisions = [dejsonify_revision(revision) for revision in page.revisions]

        return jsonify({"status": "success", "data": revisions, "parent": page})


def dejsonify_revision(revision):
    revision.revision = json.loads(revision.revision)

    return revision


# class Revisions(MethodView):
#     @user_can_write_pages
#     def get(self, page_id):
#         pass
