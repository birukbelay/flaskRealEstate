from flask import Blueprint, request
from flask_restx import Api, Resource
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash
import bcrypt
from packages.models.user import User
from packages import db

# from . import db

auth = Blueprint('auth', __name__)
api = Api(auth)


@api.route('/login', methods=['GET', 'POST'])
class Login(Resource):
    def get(self):
        try:
            email = request.form.get('email')
            passwd = request.form.get('password')
            user = User.query.filter_by(email=email)
            if not user:
                return "no user", 404

            # if check_password_hash(user.password, passwd):
            #     return

        except AttributeError:
            return "email or passowrd needed"


@api.route('/signup', methods=['GET', 'POST'])
class Signup(Resource):
    def post(self):
        try:
            email = request.form.get('email', None)
            password = request.form.get('password', None)

            if not email:
                return 'Missing email', 400
            if not password:
                return 'Missing password', 400

            hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

            user = User(email=email, hash=hashed)
            db.session.add(user)
            db.session.commit()
            return f'Welcome! {email}', 200
        except IntegrityError:
            # the rollback func reverts the changes made to the db ( so if an error happens after we commited changes they will be reverted )
            db.session.rollback()
            return 'User Already Exists', 400
        except AttributeError:
            return 'Provide an Email'
