from flask import Blueprint
from flask_restx import Api

from src.rest.auth_api import auth_ns
from src.rest.user_api import user_ns

api_bp = Blueprint('api', __name__, url_prefix="/api/v1")
authorizations = {"Bearer": {"type": "apiKey", "in": "header", "name": "Authorization"}}

api = Api(
    api_bp,
    version="1.0",
    title="House sell and buy API with JWT-Based Authentication",
    description="Welcome to the Swagger UI documentation site!",
    doc="/ui",
    authorizations=authorizations,
)

api.add_namespace(auth_ns, path='')
api.add_namespace(user_ns, path='/user')
