from flask import Blueprint, render_template, request, flash, jsonify
from flask_restx import Api, fields, Resource, Namespace

from src.domain.house import get_allHouse, create_house, get_one_house, delete_house, update_house
from src.rest.dto.house import house_model, create_house_reqParser, update_house_reqparser
from src.utils.loging import autolog

house_ns = Namespace(name="house", validate=True)
house_ns.models[house_model.name]=house_model

@house_ns.route('/', methods=['GET', 'POST'])
class HouseList(Resource):

    @house_ns.marshal_with(house_model)
    def get(self, **kwargs):
        try:
            result = get_allHouse()
            if result.failure:
                return {"faild to get houses"}, 400
            return result.value, 200
        except Exception as e:
            return "error"
    @house_ns.expect(create_house_reqParser)
    def post(self):
        house_dict= create_house_reqParser.parse_args()
        result = create_house(house_dict)
        if result.failure:
            autolog("failed result detected", result.error)
            # errs = json.dumps(result.error.__dict__)
            return {"error"}, 400
        return {"house":result.value}, 201




@house_ns.route('/<id>', endpoint= "house")
class House(Resource):
    @house_ns.marshal_with(house_model)
    def get(self, id):
        result = get_one_house(id)
        if result.failure:
            return {"faild to get user"}, 400
        return result.value, 200

    @house_ns.marshal_with(house_model)
    def post(self, id):
        user_dict = update_house_reqparser.parse_args()
        result = update_house(id, user_dict)
        if result.failure:
            return {"failed to update"}, 400
        return result.value, 201
    @house_ns.marshal_with(house_model)
    def delete(self, id):
        result = delete_house(id)
        if result.failure:
            return {"failed to delete"}, 400
        return result.value, 204