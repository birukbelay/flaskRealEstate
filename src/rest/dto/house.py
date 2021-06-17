from flask_restx import Model
from flask_restx.fields import Integer, String, Float
from flask_restx.reqparse import RequestParser

from src.utils.date import utc_now

create_house_reqParser =  RequestParser(bundle_errors=True)

create_house_reqParser.add_argument(
    "description", type=str, location="form", required=False, nullable=True,
    case_sensitive=True, default="description one"
)
create_house_reqParser.add_argument(
    "type", type=str, location="form", required=False, nullable=True,
    case_sensitive=True, default="sell"
)
create_house_reqParser.add_argument(
    "price", type=float, location="form", required=False, nullable=True,
    case_sensitive=True, default=2000000
)
create_house_reqParser.add_argument(
    "area_name", type=str, location="form", required=False, nullable=True,
    case_sensitive=True, default="mojo"
)
create_house_reqParser.add_argument(
    "picture", type=str, location="form", required=False, nullable=True,
    case_sensitive=True, default = "1.jpg"
)
create_house_reqParser.add_argument(
    "posted_date", type=str, location="form", required=False, nullable=True,
    case_sensitive=True,
)
create_house_reqParser.add_argument(
    "owner_id", type=str, location="form", required=False, nullable=True,
    case_sensitive=True, default=1
)

update_house_reqparser = create_house_reqParser.copy()


house_model = Model(
    "User",
    {
        "id" : Integer,
        "description": String,
        "type": String,
        "price": Float,
        "picture": String,
        "area_name": String,

    },
)
