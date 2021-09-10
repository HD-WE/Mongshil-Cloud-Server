from flask import Flask
from sqlalchemy import create_engine
from .model.user_dao import UserDao
from .model.child_dao import ChildDao

from .service.user_service import UserService
from .service.child_service import ChildService

import config

class Service:
    pass

def register_blueprint(app : Flask, service):
    from .view.user_view import UserView
    app.register_blueprint(UserView.user_blueprint)

    from .view.child_view import child_view
    child_blueprint = child_view(service.child_service)
    app.register_blueprint(child_blueprint)

def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_pyfile('../config.py')

    db = create_engine(app.config['DB_URL'], encoding='utf-8')

    ## Persistenace Layer
    user_dao = UserDao(db)
    child_dao = ChildDao(db)

    ## Business Layer
    service = Service
    service.user_service = UserService(user_dao, config) # config는 jwt token을 위해 필요함
    service.child_service = ChildService(child_dao)
    

    register_blueprint(app, service)

    return app