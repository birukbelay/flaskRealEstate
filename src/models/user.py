from werkzeug.security import generate_password_hash
from flask import current_app
from src import db
from uuid import uuid4

from src.utils.date import utc_now
from src.utils.loging import autolog
from src.utils.passowrd import compare_password


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(150))

    email = db.Column(db.String(150), unique=True)
    password_hash = db.Column(db.String(150))
    profile = db.Column(db.String(255))

    role = db.Column(db.String(10), default="user")
    public_id = db.Column(db.String(36), unique=True, default=lambda: str(uuid4()))
    registered_on = db.Column(db.DateTime, default=utc_now)
    # def __init__(self, first_name, email, password):
    #     self.first_name = first_name
    #     self.email = email
    #     self.password_hash=password

    def __repr__(self):
        return f"public_id:{self.public_id}, email: {self.email}, name: {self.first_name},"


    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


    def update(self):
        db.session.commit()

    def check_password(self, password):
        autolog(self.password_hash, password)
        return compare_password(self.password_hash, password)

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_public_id(cls, public_id):
        return cls.query.filter_by(public_id=public_id).first()

