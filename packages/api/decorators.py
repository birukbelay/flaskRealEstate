from functools import wraps

from flask import session, request


def _check_access_token(admin_only):
    token = request.headers.get("Authorization")
    if not token:
        raise ApiUnauthorized(description="Unauthorized", admin_only=admin_only)
    result = User.decode_access_token(token)
    if result.failure:
        raise ApiUnauthorized(
            description=result.error,
            admin_only=admin_only,
            error="invalid_token",
            error_description=result.error,
        )
    return result.value




def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if(session.get('user')):
            return f(*args, **kwargs)
        else:
            return "Not Authorized", 400
    return decorated