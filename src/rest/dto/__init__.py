import re

from flask_restx import Model
from flask_restx.fields import Nested, Boolean, Integer, List, String
from flask_restx.inputs import positive, email
from flask_restx.reqparse import RequestParser


def widget_name(name):
    """Validation method for a string containing only letters, numbers, '-' and '_'."""
    if not re.compile(r"^[\w-]+$").match(name):
        raise ValueError(
            f"'{name}' contains one or more invalid characters. Widget name must "
            "contain only letters, numbers, hyphen and underscore characters."
        )
    return name


user_reqparser = RequestParser(bundle_errors=True)

user_reqparser.add_argument(
    name="email", type=email(), location="form", required=True, nullable=False
)
user_reqparser.add_argument(
    name="password", type=str, location="form", required=True, nullable=False,
)


# user request parser
pagination_reqparser = RequestParser(bundle_errors=True)
pagination_reqparser.add_argument("page", type=positive, required=False, default=1)
pagination_reqparser.add_argument(
    "per_page", type=positive, required=False, choices=[5, 10, 25, 50, 100], default=10, help='Bad choice: {error_msg}'
)

# models, user models


pagination_links_model = Model(
    "Nav Links",
    {"self": String, "prev": String, "next": String, "first": String, "last": String},
)

pagination_model = Model(
    "Pagination",
    {
        "links": Nested(pagination_links_model, skip_none=True),
        "has_prev": Boolean,
        "has_next": Boolean,
        "page": Integer,
        "total_pages": Integer(attribute="pages"),
        "items_per_page": Integer(attribute="per_page"),
        "total_items": Integer(attribute="total"),

    },
)
