from src import db


class House(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text, nullable=True)
    type = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=True)
    picture = db.Column(db.String, nullable=False)
    area_name = db.Column(db.String, nullable=False)
    posted_date = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.JSON)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
