from flask import Blueprint, request, json
from flask_jwt_extended import jwt_required
from extension import mongo
from api.app.Users.HandlerDetectUserFace import detect as dt, detect_test
from api.app.Helper.JSONEncoder import JSONEncoder

detect = Blueprint('detect', __name__)

@detect.route('/facedetect', methods=['POST'])
def post():
    id = request.args['a_id']
    return json.dumps(dt(request.form['File'], id), cls=JSONEncoder)

@detect.route('/facedetect/test', methods=['POST'])
def dt_test():
    print(detect_test(request.form['File']))
    return 'ok'
