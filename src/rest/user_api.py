import http
from http import HTTPStatus

from flask import Blueprint, request, jsonify
from flask_restx import Api, fields, Resource, Namespace, marshal

from src.domain.decorators import token_required
from src.domain.user import create_user
from src.models.user import User
from src import db
from src.rest.dto import pagination_reqparser, pagination_links_model, pagination_model
from src.rest.dto.users import user_model, create_user_reqparser, users_pagination_model, users_List_model
from src.utils.loging import autolog

user_ns = Namespace(name="user", validate=True)
user_ns.models[user_model.name] = user_model
user_ns.models[pagination_links_model.name] = pagination_links_model
user_ns.models[pagination_model.name] = pagination_model
user_ns.models[users_pagination_model.name] = users_pagination_model
user_ns.models[users_List_model.name] = users_List_model


# user = api.model('Model', {
#     'name': fields.String(attribute='first_name'),
#     'email': fields.String,
# })
# api.models[user_model.name] = user_model


@user_ns.route("", endpoint="users")
class UsersApi(Resource):
    """Handles HTTP requests to URL: /users."""

    @user_ns.doc(security="Bearer")
    @user_ns.expect(create_user_reqparser)
    def post(self):
        user_dict = create_user_reqparser.parse_args()

        result = create_user(user_dict)
        if result.failure:
            autolog(f"log on fail===<> err={result.error} , value{result.value}")
            print(">////mes", result.value,"err", result.error)
            return _create_response(HTTPStatus.UNAUTHORIZED, result.error)
        return _create_response(HTTPStatus.CREATED, result.value)

    @user_ns.doc(security="Bearer")
    @user_ns.response(HTTPStatus.OK, "Retrieved user list.", users_List_model)
    @user_ns.expect(pagination_reqparser)
    # @user_ns.marshal_with(users_List_model, )
    def get(self, **kwargs):
        try:
            users = User.query.all()
            print("usrs are -----|",users)
            response_data = marshal(users, users_List_model)
            return response_data
        except Exception as e:
            print("======:> er", e)
            return "error"
        # return  {"name":usrs.first_name, 'email':usrs.email}


def _create_response(status_code, message):
    response = jsonify(
        status=http.HTTPStatus(status_code),
        message=message,

    )
    response.status_code = status_code
    return response

    # response.status_code = HTTPStatus.CREATED
    # response.headers["Location"] = url_for("api.widget", name=email)
    # return response
