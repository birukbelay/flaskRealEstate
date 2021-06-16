import http
import json
from http import HTTPStatus

from flask import Blueprint, request, jsonify
from flask_restx import Api, fields, Resource, Namespace, marshal

from src.domain.decorators import token_required
from src.domain.user import create_user, get_one_user, update_user, delete_user, get_alluser
from src.models.user import User
from src import db
from src.rest.dto import pagination_reqparser, pagination_links_model, pagination_model
from src.rest.dto.users import user_model, create_user_reqparser, users_pagination_model, users_List_model, \
    update_user_reqparser
from src.utils.loging import autolog, autolog_plus

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
class UsersList(Resource):
    """Handles HTTP requests to URL: /users."""

    @user_ns.doc(security="Bearer")
    @user_ns.expect(create_user_reqparser)
    def post(self):
        try:
            user_dict = create_user_reqparser.parse_args()

            result = create_user(user_dict)

            if result.failure:
                autolog("failed result detected", result.error.args)
                # errs = json.dumps(result.error.__dict__)
                return _create_error_response(HTTPStatus.BAD_REQUEST, result.error.args)
            return _create_response(HTTPStatus.CREATED, result.value)
        except Exception as e:
            return _create_error_response(HTTPStatus.INTERNAL_SERVER_ERROR, e.args)


    @user_ns.response(HTTPStatus.OK, "Retrieved user list.", users_List_model)
    @user_ns.expect(pagination_reqparser)
    @user_ns.marshal_with(user_model)
    def get(self):
        try:
            request_data = pagination_reqparser.parse_args()
            result = get_alluser()
            if result.failure:
                return {"faild to get user"}, 400
            return result.value, 200
        except Exception as e:
            print("======:> er", e.args)
            return "error"
        # return  {"name":usrs.first_name, 'email':usrs.email}

@user_ns.route("/<id>", endpoint="user")
class User_Api(Resource):
    @user_ns.marshal_with(user_model)
    def get(self, id):
        result = get_one_user(id)
        if result.failure:
            return {"faild to get user"}, 400
        return result.value, 200

    # @user_ns.expect(update_user_reqparser)
    @user_ns.marshal_with(user_model)
    def post(self, id):
        user_dict = update_user_reqparser.parse_args()
        result = update_user(id, user_dict)
        if result.failure:
            return {"failed to update"}, 400
        return result.value, 201
    @user_ns.marshal_with(user_model)
    def delete(self, id):
        result = delete_user(id)
        if result.failure:
            return {"failed to delete"}, 400
        return result.value, 204





def _create_error_response(status_code, message):
    autolog_plus("error:", message)
    response = jsonify(
        status=http.HTTPStatus(status_code),
        message="error",

    )
    response.status_code = status_code
    return response


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
