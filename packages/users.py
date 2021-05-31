from flask import Blueprint, render_template, request, flash, jsonify
from flask_restx import Api, fields, Resource
from .models import User
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
        return User.query.all()
        # return  {"name":usrs.first_name, 'email':usrs.email}

    def post(self):
        if request.method == 'POST':
            name = request.form.get('name')
            email = request.form.get('email')

            user = User(first_name=name, email=email)
            db.session.add(user)
            db.session.commit()
            return {"name":user.first_name, 'email':user.email}
