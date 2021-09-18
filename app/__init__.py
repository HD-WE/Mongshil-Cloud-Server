from app.view import user
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from flask_login import LoginManager, current_user

import config
import os

def register_blueprint(app : Flask):
    from .view.child import child_blueprint
    app.register_blueprint(child_blueprint)

    from .view.parents import parents_blueprint
    app.register_blueprint(parents_blueprint)

    from .view.user import user_blueprint
    app.register_blueprint(user_blueprint)

def create_app() -> Flask:
    app = Flask(__name__)
    app.secret_key = "12341234213"
    app.config["SQLALCHEMY_DATABASE_URI"] = config.DB_URL
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.unauthorized_handler
    def unauthorized():
        return "You must be logged in to access this content.", 403

    db = SQLAlchemy(app)

    register_blueprint(app)

    return app