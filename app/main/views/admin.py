from flask import render_template
from flask.views import MethodView
from utils.acl import user_has_role

class Admin(MethodView):

    @user_has_role('administrator')
    def get(self):
        return render_template('main/admin.html')
