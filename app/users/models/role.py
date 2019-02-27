from app import db

role_user = db.Table(
    "role_user",
    db.Column("role_id", db.Integer(), db.ForeignKey("role.id")),
    db.Column("user_id", db.Integer(), db.ForeignKey("user.id")),
)


class Role(db.Model):
    visible = ['id', 'name', 'display_name', 'description']

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    display_name = db.Column(db.String(255), unique=True)
    description = db.Column(db.String(255))

    # Representation
    def __repr__(self):
        return f"Role('{self.name}', '{self.display_name}', '{self.description}')"
