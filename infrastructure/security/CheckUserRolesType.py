from flask_jwt_extended import get_jwt_claims


def check_roles_user(role):
    roles = get_jwt_claims()['role']
    for r in roles:
        if r == role:
            return True
    return False
