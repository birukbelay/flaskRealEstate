from sqlalchemy.exc import IntegrityError

from src import db
from src.domain.decorators import token_required
from src.models.user import User
from src.utils.loging import autolog
from src.utils.result import Result


# @token_required
def create_user(user_dict):
    try:
        email = user_dict["email"]
        autolog(f"email={email}")
        if User.find_by_email(email):
            error = f"Email: {email} already exists, must be unique."
            return Result.Fail(error)
        user = User(**user_dict)
        autolog(f"log on fail===<> err={result.error} , value{result.value}")
        autolog(user)

        db.session.add(user)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return Result.Fail("db Error")
    except Exception as e:
        return Result.Fail(e)
    return Result.Ok(user.__repr__())


# def get_users_list(page, per_page):
#     pagination = User.query.paginate(page, per_page, error_out=False)
#     if not user:
#         return Result.Fail("email or password does not match")
#     access_token = encode_access_token(user.id, user.role)
#     return Result.Ok(access_token)
