from flask import url_for, jsonify
from flask_restx import marshal
from sqlalchemy.exc import IntegrityError

from src import db
from src.domain.decorators import token_required
from src.models.user import User
from src.rest.dto import pagination_model
from src.rest.dto.users import users_pagination_model
from src.utils.loging import autolog
from src.utils.passowrd import generate_hash
from src.utils.result import Result



@token_required
def create_user(user_dict):
    try:
        email = user_dict["email"]
        passw = user_dict["password"]

        # calls generate hash function to return the hash of the password
        user_dict["password_hash"]= generate_hash(passw)

        if User.find_by_email(email):
            error = f"Email: {email} already exists, must be unique."
            return Result.Fail(error)

        user_dict.pop("password")
        user_dict.pop("file")

        # user=User(email=email, password_hash=)
        user = User(**user_dict)

        db.session.add(user)
        db.session.commit()
        return Result.Ok(user.__repr__())
    except IntegrityError:
        db.session.rollback()
        return Result.Fail("db Error")
    except Exception as e:
        return Result.Fail(e)

def get_alluser():
    try:
        users = User.query.all()
        return Result.Ok(users)
    except Exception as e:
        return Result.Fail(e)

def get_one_user(id):
    try:
        user = User.query.get_or_404(id)
        return Result.Ok(user)
    except Exception as e:
        return Result.Fail(e)

def delete_user(id):
    try:
        user = User.query.get_or_404(id)
        if not user:
            return Result.Fail("no user by this id")
        db.session.delete(user)
        db.session.commit()
        return Result.Ok("user deleted")
    except Exception as e:
        return Result.Fail(e)

def update_user(id, user_dict):
    try:
        user = User.query.get_or_404(id)
        if not user:
            return Result.Fail("no user by this id")
        for k, v in user_dict.items():
            setattr(user, k, v)
        db.session.commit()
        message = f"'{id}' was successfully updated"
        return Result.Ok(message)
    except Exception as e:
        return Result.Fail(e)



#
# def get_users_paginated_list(page, per_page):
#     try:
#         a= User.query.findall()
#         pagination = User.query.paginate(page, per_page, error_out=False)
#
#         response_data = marshal(pagination, users_pagination_model)
#         autolog("pag-", response_data)
#
#         response_data["links"] = _pagination_nav_links(pagination)
#
#         response_data["Link"] = _pagination_nav_header_links(pagination)
#         response_data["Total-Count"] = pagination.total
#
#         return Result.Ok(a)
#     except Exception as e:
#         return Result.Fail(e)
#
#
#
# def _pagination_nav_links(pagination):
#     nav_links = {}
#     per_page = pagination.per_page
#     this_page = pagination.page
#     last_page = pagination.pages
#     nav_links["self"] = url_for("api.users", page=this_page, per_page=per_page)
#     nav_links["first"] = url_for("api.users", page=1, per_page=per_page)
#     if pagination.has_prev:
#         nav_links["prev"] = url_for(
#             "api.users", page=this_page - 1, per_page=per_page
#         )
#     if pagination.has_next:
#         nav_links["next"] = url_for(
#             "api.users", page=this_page + 1, per_page=per_page
#         )
#     nav_links["last"] = url_for("api.users", page=last_page, per_page=per_page)
#     return nav_links
#
#
# def _pagination_nav_header_links(pagination):
#     url_dict = _pagination_nav_links(pagination)
#     link_header = ""
#     for rel, url in url_dict.items():
#         link_header += f'<{url}>; rel="{rel}", '
#     return link_header.strip().strip(",")
