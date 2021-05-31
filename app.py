from flask import Flask
from flask_restx import Api, Resource, fields

app = Flask(__name__)
api = Api(app)

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
        return {'name': 'name1', 'address':"address one"}  # Some function that queries the db

@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

if __name__ == '__main__':
    app.run(debug=True)