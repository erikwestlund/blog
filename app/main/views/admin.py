from flask import render_template
from flask.views import MethodView

class Admin(MethodView):

    def get(self):
        return render_template('main/admin.html')
