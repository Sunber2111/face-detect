from flask_jwt_extended import get_jwt_identity

def get_user_id():
    return get_jwt_identity()