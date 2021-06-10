from flask import Blueprint, render_template, request, flash, jsonify
from flask_restx import Api, fields, Resource
from .models.user import User
from . import db

users = Blueprint('views', __name__)
api = Api(users)

user = api.model('Model', {
    'name': fields.String(attribute='first_name'),
    'email': fields.String,

})


@api.route('/', methods=['GET', 'POST'])
class UserApi(Resource):
    @api.marshal_with(user, envelope='resource')
    def get(self, **kwargs):
        try:
            users = User.query.all()
            print(users)
            return users
        except Exception as e:
            print("======:> er")
            return {"error"}
        # return  {"name":usrs.first_name, 'email':usrs.email}

    def post(self):
        if request.method == 'POST':
            print("-----------------------", "heere")
            name = request.form.get('name')
            email = request.form.get('email')
            try:
                user = User(first_name=name, email=email)
                db.session.add(user)
                db.session.commit()
            except Exception as e:
                print("======:> er", e)

                return {"error"}
            return {"name": name, 'email': email}
