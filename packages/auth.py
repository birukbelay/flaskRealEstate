from flask import Blueprint, request
from flask_restx import Api, Resource

# from .models import User
# from werkzeug.security import generate_password_hash, check_password_hash
# from . import db

auth = Blueprint('auth', __name__)
api = Api(auth)

@api.route('/hello', methods=['GET', 'POST'])
class Login(Resource):
    def get(self):
        return {"hello": "world"}

@api.route('/login', methods=['GET', 'POST'])
class Login(Resource):
    def get(self):
        if request.method == 'POST':
            email = request.form.get('email')
            password = request.form.get('password')
            return {"method": "Post", "email": email, "pass": password}

        return {"method": "GET", "email": "", "pass": ""}
