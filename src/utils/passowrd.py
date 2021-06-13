from werkzeug.security import check_password_hash, generate_password_hash


def compare_password(password_one, password):
    return check_password_hash(password_one, password)


def generate_hash(password):
    return generate_password_hash(password, 'sha256', 15)
