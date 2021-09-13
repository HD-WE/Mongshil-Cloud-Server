from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

import config

def register_blueprint(app : Flask):
    from .view.child import child_blueprint
    app.register_blueprint(child_blueprint)

    from .view.parents import parents_blueprint
    app.register_blueprint(parents_blueprint)

def create_app() -> Flask:
    app = Flask(__name__)
    app.secret_key = "12341234213"
    app.config["SQLALCHEMY_DATABASE_URI"] = config.DB_URL
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db = SQLAlchemy(app)

    register_blueprint(app)

    return app