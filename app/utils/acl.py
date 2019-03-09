from functools import wraps

from flask import flash, redirect, url_for, abort
from flask_login import current_user


def user_has_role(role):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.is_authenticated:
                abort(403)

            if not current_user.has_role(role):
                abort(403)

            return f(*args, **kwargs)

        return decorated_function

    return decorator


def user_can_write_posts(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated:
            abort(403)

        if not (current_user.has_role("administrator") or current_user.has_role("writer")):
            abort(403)

        return f(*args, **kwargs)

    return decorated_function

