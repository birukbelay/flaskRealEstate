from werkzeug.security import generate_password_hash
from flask import current_app
from src import db


from src.utils.passowrd import compare_password


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(150))
    public_id = db.Column(db.String(150))
    email = db.Column(db.String(150), unique=True)
    password_hash = db.Column(db.String(150))
    role = db.Column(db.String(10), default="user")

    # houses = db.relationship('House', backref='user')

    # def __init__(self, first_name, email, password):
    #     self.first_name = first_name
    #     self.email = email
    #     self.password_hash=password

    def __repr__(self):
        return {
            'id': self.id,
            'email': self.email,
            'name': self.first_name,
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def check_password(self, password):
        return compare_password(self.password_hash, password)

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_public_id(cls, public_id):
        return cls.query.filter_by(id=public_id).first()


