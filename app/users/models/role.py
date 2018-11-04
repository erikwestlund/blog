from app import db
from utils.model_accessor_mixin import ModelAccessorMixin

roles_users = db.Table('roles_users',
                       db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
                       db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))


class Role(db.Model, ModelAccessorMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    display_name = db.Column(db.String(255), unique=True)
    description = db.Column(db.String(255))

    # Representation
    def __repr__(self):
        return f"Role('{self.name}', '{self.display_name}', '{self.description}')"

