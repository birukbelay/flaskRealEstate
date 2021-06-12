from functools import wraps
from werkzeug.exceptions import Unauthorized, Forbidden
from flask import session, request, current_app
from datetime import datetime, timezone, timedelta

import jwt

from src.utils.result import Result


def token_required(f):
    """Execute function if request contains valid access token."""

    @wraps(f)
    def decorated(*args, **kwargs):
        token_payload = _check_access_token(admin_only=False)
        for name, val in token_payload.items():
            setattr(decorated, name, val)
        return f(*args, **kwargs)

    return decorated


def admin_token_required(f):
    """Execute function if request contains valid access token AND user is admin."""

    @wraps(f)
    def decorated(*args, **kwargs):
        token_payload = _check_access_token(admin_only=True)
        if not token_payload["role"] == 'admin':
            raise Forbidden()
        for name, val in token_payload.items():
            setattr(decorated, name, val)
        return f(*args, **kwargs)

    return decorated


def _check_access_token(admin_only):
    token = request.headers.get("Authorization")
    if not token:
        raise Unauthorized(description="Unauthorized")
    result = decode_access_token(token)
    if result.failure:
        raise Unauthorized(
            description=result.error,
            www_authenticate=(admin_only, "invalid_token", result.error,)
        )
    return result.value


def decode_access_token(access_token):
    if isinstance(access_token, bytes):
        access_token = access_token.decode("ascii")
    if access_token.startswith("Bearer "):
        split = access_token.split("Bearer")
        access_token = split[1].strip()
    try:
        key = current_app.config.get("SECRET_KEY")
        payload = jwt.decode(access_token, key, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        error = "Access token expired. Please log in again."
        return Result.Fail(error)
    except jwt.InvalidTokenError:
        error = "Invalid token. Please log in again."
        return Result.Fail(error)

    user_dict = dict(
        id=payload["sub"],
        role=payload["role"],
        token=access_token,
        expires_at=payload["exp"],
    )
    return Result.Ok(user_dict)


def encode_access_token(id, role):
    now = datetime.now(timezone.utc)
    token_age_h = current_app.config.get("TOKEN_EXPIRE_HOURS")
    token_age_m = current_app.config.get("TOKEN_EXPIRE_MINUTES")
    expire = now + timedelta(hours=token_age_h, minutes=token_age_m)

    if current_app.config["TESTING"]:
        expire = now + timedelta(seconds=5)

    payload = dict(exp=expire, iat=now, sub=id, role=role)
    key = current_app.config.get("SECRET_KEY")
    return jwt.encode(payload, key, algorithm="HS256")
