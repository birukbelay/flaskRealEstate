from src import db
from src.models.user import User
from sqlalchemy.exc import IntegrityError

from src.domain.decorators import encode_access_token
from src.utils.loging import autolog
from src.utils.passowrd import generate_hash
from src.utils.result import Result


def process_login(email, password):
    user = User.find_by_email(email)

    # checks if the user exists
    if not user:
        return Result.Fail("email or password does not match")
    # checks if the password matches
    if not user.check_password(password):
        return Result.Fail("email or password does not match")

    access_token = encode_access_token(user.id, user.role)
    return Result.Ok({"access_token" : access_token, "user": user.__repr__()})


def process_signup(email, password):
    try:
        if User.find_by_email(email):
            return Result.Fail(f"{email}  is already registered")
        new_user = User(email=email, password_hash=generate_hash(password))
        db.session.add(new_user)
        db.session.commit()
        access_token = encode_access_token(new_user.id, new_user.role)
    except IntegrityError:
        # the rollback func reverts the changes made to the db ( so if an error happens after we commited changes they will be reverted )
        db.session.rollback()
        return Result.Fail("db Error")
    except Exception as e:
        return Result.Fail(e)
    return Result.Ok(access_token)
