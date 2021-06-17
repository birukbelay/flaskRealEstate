from src import db

# from .user import db
from src.utils.date import utc_now


class House(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text, nullable=True)
    type = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=True)
    picture = db.Column(db.String, nullable=False)
    area_name = db.Column(db.String, nullable=False)
    posted_date = db.Column(db.DateTime, nullable=False, default=utc_now)
    location = db.Column(db.JSON)

    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    owner = db.relationship("User", backref=db.backref("houses"))

    def __repr__(self):
        return f"id:{self.id}, description: {self.description}, price: {self.price}, user_id:{self.owner_id}"