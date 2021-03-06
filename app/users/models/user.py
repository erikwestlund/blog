from flask import current_app
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from sqlalchemy.sql import func

from app import db
from app import login_manager
from users.models.role import role_user
from utils.models.timestamps import TimestampMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin, TimestampMixin):

    visible = [
        "id",
        "username",
        "email",
        "display_name",
        "first_name",
        "last_name",
        "created_at",
    ]

    id = db.Column(db.Integer, primary_key=True)

    # User authentication information (required for Flask-User)
    username = db.Column(db.String(50), nullable=False, server_default="", unique=True)
    email = db.Column(db.Unicode(255), nullable=False, server_default="", unique=True)
    password = db.Column(db.String(255), nullable=False, server_default="")

    active = db.Column(db.Boolean(), nullable=False, server_default="0")

    # User information
    first_name = db.Column(db.Unicode(50), nullable=False, server_default="")
    last_name = db.Column(db.Unicode(50), nullable=False, server_default="")
    about = db.Column(db.Text, nullable=False, server_default="")

    # Timestamps
    email_confirmed_at = db.Column(db.DateTime())

    # Relationships
    roles = db.relationship("Role", secondary=role_user, cascade="save-update")

    def has_role(self, role):
        return True if role in [role.name for role in self.roles] else False

    # Is confirmed
    @property
    def email_confirmed(self):
        return True if self.email_confirmed_at else False

    @property
    def name(self):
        return (self.first_name + " " + self.last_name).strip()

    @property
    def display_name(self):
        if self.first_name:
            return self.first_name.strip()
        else:
            return self.username

    # Token generator
    def generate_token(self, expires_sec=1800):
        s = Serializer(current_app.config["SECRET_KEY"], expires_sec)
        return s.dumps({"user_id": self.id}).decode("utf-8")

    # Generate a confirmation token
    def generate_confirmation_token(self, expires_sec=86400):
        return self.generate_token(expires_sec=expires_sec)

    # Generate a password reset token
    def generate_password_reset_token(self, expires_sec=1800):
        return self.generate_token(expires_sec=expires_sec)

    @staticmethod
    def verify_token(token):
        s = Serializer(current_app.config["SECRET_KEY"])
        try:
            user_id = s.loads(token)["user_id"]
        except:
            return None
        return User.query.get(user_id)

    # Representation
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.first_name}', '{self.last_name}')"
