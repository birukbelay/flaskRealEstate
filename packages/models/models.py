from packages import db


#

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)

    first_name = db.Column(db.String(150))
    email = db.Column(db.String(150), unique=True)

    password = db.Column(db.String(150))

    def __init__(self, first_name, email):
        self.first_name = first_name
        self.email = email

    def details(self):
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


if __name__ == '__main__':
    db.drop_all()
    db.create_all()
