from app import db
from app import login_manager
from users.models.role import roles_users
from flask import current_app
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from sqlalchemy.sql import func


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)

    # User authentication information (required for Flask-User)
    username = db.Column(db.String(50), nullable=False, server_default=u'', unique=True)
    email = db.Column(db.Unicode(255), nullable=False, server_default=u'', unique=True)
    password = db.Column(db.String(255), nullable=False, server_default='')

    active = db.Column(db.Boolean(), nullable=False, server_default='0')

    # User information
    first_name = db.Column(db.Unicode(50), nullable=False, server_default=u'')
    last_name = db.Column(db.Unicode(50), nullable=False, server_default=u'')

    # Timestamps
    email_confirmed_at = db.Column(db.DateTime())
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, onupdate=func.now())

    # Relationships
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))

    # Token generator
    def generate_token(self, expires_sec=86400):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    # Generate a confirmation token
    def generate_confirmation_token(self, expires_sec=86400):
        return self.generate_token(expires_sec=expires_sec)

    # Generate a password reset token
    def generate_confirmation_token(self, expires_sec=1800):
        return self.generate_token(expires_sec=expires_sec)

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    # Representation
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.first_name}', '{self.last_name}')"
