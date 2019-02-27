from flask import render_template, request
from flask.views import MethodView

class Index(MethodView):
    def get(self):
        page = request.args.get('page') or 1

        return render_template("main/index.html", page=page)
