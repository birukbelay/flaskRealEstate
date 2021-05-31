from flask import Blueprint, render_template, request, flash, jsonify
from flask_restx import Api, fields, Resource

users = Blueprint('views', __name__)
api = Api(users)


@api.route('/', methods=['GET', 'POST'])
class Main(Resource):
    def get(self, **kwargs):
        if request.method == 'POST':
            return {"method": "POst", "user": "", "pass": ""}

        return {"method": "GET", "email": "", "pass": ""}


class UnreadItem(fields.Raw):
    def format(self, value):
        return "Unread" if value & 0x02 else "Read"


class AllCapsString(fields.Raw):
    def format(self, value):
        return value.upper()


todo_model = api.model('Model', {
    'name': fields.String,
    'all_caps_name': AllCapsString(attribute='name'),
    'address': fields.String,
    'status': UnreadItem(attribute='flags'),
    'date_updated': fields.DateTime(dt_format='rfc822'),
})


@api.route('/todo')
class Todo(Resource):
    @api.marshal_with(todo_model, envelope='resource')
    def get(self, **kwargs):
        return {'name': 'name1', 'address': "address one"}  # Some function that queries the db
