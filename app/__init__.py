from flask import Flask
from sqlalchemy import create_engine
from .model.user_dao import UserDao
from .service.user_service import UserService

import config

class Service:
    pass

def register_blueprint(app : Flask):
    from .view.user_view import UserView
    app.register_blueprint(UserView.user_blueprint)

def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_pyfile('../config.py')

    db = create_engine(app.config['DB_URL'], encoding='utf-8')

    ## Persistenace Layer
    user_dao = UserDao(db)

    ## Business Layer
    service = Service
    service.user_service = UserService(user_dao, config) # config는 jwt token을 위해 필요함

    register_blueprint(app)

    return app