from . import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)

    first_name = db.Column(db.String(150))
    password = db.Column(db.String(150))

