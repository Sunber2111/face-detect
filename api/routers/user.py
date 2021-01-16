from flask import Blueprint, request, json
from flask_jwt_extended import jwt_required
from infrastructure.security.JwtGennerate import create_token
from infrastructure.security.GetUserId import get_user_id
from extension import model_predict

user = Blueprint('user', __name__)

@user.route('/user/current', methods=['GET'])
@jwt_required
def current_user():
    new_token = create_token(get_user_id())
    userId = get_user_id()
    return json.dumps({'token': new_token, 'userId': userId}), 200


@user.route('/user/add_new_user', methods=['POST'])
def add_new_user_face():
    model_predict.training_new_face(request.form, '5fae0373ee82e9f4b1b6007b')
    return json.dumps({'token': 'ok'}), 200

