from packages import db


class House(db.Model):
    __tablename__ = 'houses'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text, nullable=True)
    type = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=True)
    picture = db.Column(db.String, nullable=False)
    area_name = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    posted_date = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.JSON)
