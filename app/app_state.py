from flask_login import current_user

def app_state():
    if current_user:
        logged_in = current_user.is_authenticated
        username = current_user.username if current_user.is_authenticated else 'My Account'
    else:
        logged_in = 0
        username = 'My Account'
    return dict(
        state={
            'user': {
                'logged_in': logged_in,
                'username': username
            }
        }
    )