from functools import wraps

from flask import flash, redirect, url_for
from flask_login import current_user


def user_has_role(role):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.has_role(role):
                flash("Access denied.")
                return redirect(url_for('main.index'))
            return f(*args, **kwargs)
        return decorated_function
    return decorator
