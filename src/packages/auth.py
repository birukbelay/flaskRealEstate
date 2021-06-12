from src import db
from src.models.user import User
from sqlalchemy.exc import IntegrityError

from src.packages.decorators import encode_access_token
from src.utils.result import Result


def process_login(email, password):
    user = User.find_by_email(email)
    if not user or not user.check_password(password):
        return Result.Fail("email or password does not match")
    access_token = encode_access_token(user.id, user.role)
    return Result.Ok(access_token)


def process_signup(email, password):
    try:
        if User.find_by_email(email):
            return Result.Fail(f"{email} is already registered")

        new_user = User(email=email, password_hash=password)
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
