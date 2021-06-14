"""Parsers and serializers for /users API endpoints."""
from flask_restx import Model
from flask_restx.fields import String, Boolean, Nested, Integer, List
from flask_restx.inputs import email, URL, positive
from flask_restx.reqparse import RequestParser
from werkzeug.datastructures import FileStorage

from src.rest.dto import widget_name, pagination_model, user_reqparser, pagination_links_model

# request parsers


create_user_reqparser = user_reqparser.copy()
create_user_reqparser.add_argument(
    "name", type=widget_name, location="form", required=False, nullable=True,
    case_sensitive=True,
)
create_user_reqparser.add_argument(
    name="role", type=str, location="form", required=False, nullable=True
)
create_user_reqparser.add_argument(
    "profile", type=URL(schemes=["http", "https"]), location="form", required=False, nullable=True,
)
create_user_reqparser.add_argument('file', location='files', type=FileStorage, required=False)

update_user_reqparser = create_user_reqparser.copy()
update_user_reqparser.remove_argument("profile")
update_user_reqparser.replace_argument('password', required=False, nullable=True, location='json')

# response Models

user_model = Model(
    "User",
    {
        "email": String,
        "public_id": String,
        "role": String,
        "registered_on": String(attribute="registered_on"),
        "token_expires_in": String,
        "profile": String,
    },
)


users_pagination_model = Model(
    "Pagination",
    {
        "links": Nested(pagination_links_model, skip_none=True),
        "has_prev": Boolean,
        "has_next": Boolean,
        "page": Integer,
        "total_pages": Integer(attribute="pages"),
        "items_per_page": Integer(attribute="per_page"),
        "total_items": Integer(attribute="total"),
        "items": List(Nested(user_model)),
    },
)

users_List_model = Model(
    "Users_list", {
        "users": List(Nested(user_model))
})
