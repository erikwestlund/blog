from flask.views import MethodView


class ShowPage(MethodView):
    def get(self, year, month, slug):
        pass
