from flask_login import current_user

def app_state():
    logged_in = current_user.is_authenticated if current_user else 0
    is_admin = current_user.has_role('administrator') if current_user and current_user.is_authenticated else 0
    username = current_user.username if current_user and current_user.is_authenticated else 'My Account'
    email = current_user.email if current_user and  current_user.is_authenticated else None
    first_name = current_user.first_name if current_user and  current_user.is_authenticated else None
    last_name = current_user.last_name if current_user and  current_user.is_authenticated else None

    return dict(
        state={
            'user': {
                'logged_in': logged_in,
                'is_admin': is_admin,
                'account': {
                    'username': username,
                    'email': email,
                    'first_name': first_name,
                    'last_name': last_name,
                }
            }
        }
    )