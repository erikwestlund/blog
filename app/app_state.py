from flask_login import current_user

def app_state():
    if current_user:
        logged_in = current_user.is_authenticated
        username = current_user.username if current_user.is_authenticated else 'My Account'
        email = current_user.email if current_user.is_authenticated else None
        first_name = current_user.first_name if current_user.is_authenticated else None
        last_name = current_user.last_name if current_user.is_authenticated else None
    else:
        logged_in = 0
        username = None
        email = None
        first_name = None
        last_name = None

    return dict(
        state={
            'user': {
                'logged_in': logged_in,
                'account': {
                    'username': username,
                    'email': email,
                    'first_name': first_name,
                    'last_name': last_name,
                }
            }
        }
    )