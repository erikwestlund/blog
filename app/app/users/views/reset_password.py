from flask.views import MethodView

class ResetPassword(MethodView):

    def get(self):
        return 'Hey'