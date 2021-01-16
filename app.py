from flask import Flask
from api.routers.account import account
from api.routers.detect import detect
from api.routers.user import user
from flask_cors import CORS
from extension import mongo
from api.middlewares.handle_exception import handle_exception
from werkzeug.exceptions import HTTPException
from flask_jwt_extended import JWTManager
from services.ai.mapper import initial_mapper

def create_app():
    app = Flask(__name__)

    app.config.from_object('settings')

    CORS(app, resources={r"/api/*": {"origins": "*"}})

    app.register_blueprint(account, url_prefix='/api')
    app.register_blueprint(user, url_prefix='/api')
    app.register_blueprint(detect, url_prefix='/api')

    @app.errorhandler(HTTPException)
    def handle(e): return handle_exception(e)

    jwt = JWTManager(app)

    @jwt.expired_token_loader
    def my_expired_token_callback():
        return json.dumps({
            'status': 412,
            'description': 'Hết phiên làm việc , vui lòng đăng nhập lại',
            'name': 'Session Error'
        }), 412

    mongo.init_app(app)

    return app


if __name__ == '__main__':

    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    app = create_app()

    app.run(host='0.0.0.0', port=port)

