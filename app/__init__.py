from flask import Flask
from sqlalchemy import create_engine

from .model.user_dao import UserDao
from .model.child_dao import ChildDao
from .model.parents_dao import ParentsDao

from .service.user_service import UserService
from .service.child_service import ChildService
from .service.parents_service import ParentsService

import config

class Service:
    pass

def register_blueprint(app : Flask, service):
    from .view.user_view import UserView
    app.register_blueprint(UserView.user_blueprint)

    from .view.child_view import child_view
    child_blueprint = child_view(service.child_service)
    app.register_blueprint(child_blueprint)

    from .view.parents_view import parents_view
    parents_blueprint = parents_view(service.parents_service)
    app.register_blueprint(parents_blueprint)

def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_pyfile('../config.py')
    app.secret_key = "12341234213"

    db = create_engine(app.config['DB_URL'], encoding='utf-8')

    ## Persistenace Layer
    user_dao = UserDao(db)
    child_dao = ChildDao(db)
    parents_dao = ParentsDao(db)

    ## Business Layer
    service = Service
    service.user_service = UserService(user_dao, config) # config는 jwt token을 위해 필요함
    service.child_service = ChildService(child_dao)
    service.parents_service = ParentsService(parents_dao)

    register_blueprint(app, service)

    return app