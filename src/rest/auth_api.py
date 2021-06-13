import http
from http import HTTPStatus

from flask import Blueprint, request, jsonify, current_app
from flask_restx import Api, Resource, Namespace
from flask_restx import abort
from src.domain.auth import process_login, process_signup
from src.rest.dto import user_reqparser
from src.utils.loging import autolog

auth_ns = Namespace(name="auth", validate=True)

@auth_ns.route('/login', methods=['GET', 'POST'])
class Login(Resource):
    @auth_ns.expect(user_reqparser)
    def post(self):
        try:
            email = request.form.get('email')
            passwd = request.form.get('password')
            result = process_login(email, passwd)
            if result.failure:
                abort(HTTPStatus.UNAUTHORIZED, "email or password does not match", status="fail")
            return _create_response(result.value, HTTPStatus.OK, "successfully logged in")

        except AttributeError:
            return "email or passowrd wrong", 400
        except Exception as e:
            return {"error":e.args}, 500


@auth_ns.route('/signup', methods=['GET', 'POST'])
class Signup(Resource):
    @auth_ns.expect(user_reqparser)
    def post(self):
        try:
            email = request.form.get('email', None)
            password = request.form.get('password', None)
            if not email:
                return 'Missing email', 400
            if not password:
                return 'Missing password', 400

            result = process_signup(email, password)
            print("====", result.failure)
            if result.failure:
                # return abort(HTTPStatus.UNAUTHORIZED, "email or password does not match", status="fail")
                return _create_response("",HTTPStatus.UNAUTHORIZED ,result.error)
            res = _create_response(result.value, HTTPStatus.OK, message="successfully registered")
            return  res
        except Exception as e:
            print("err-----", e)
            return {"error":e.args}, 500


def _get_token_expire_time():
    token_age_h = current_app.config.get("TOKEN_EXPIRE_HOURS")
    token_age_m = current_app.config.get("TOKEN_EXPIRE_MINUTES")
    expires_in_seconds = token_age_h * 3600 + token_age_m * 60
    return expires_in_seconds if not current_app.config["TESTING"] else 5


def _create_response(token, status_code, message):
    response = jsonify(
        status=http.HTTPStatus(status_code),
        message=message,
        access_token=token,
        token_type="bearer",
        expires_in=_get_token_expire_time(),
    )
    response.status_code = status_code
    response.headers["Cache-Control"] = "no-store"
    response.headers["Pragma"] = "no-cache"
    return response
