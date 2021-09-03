from flask import Flask

def create_app() -> Flask:
    flask_app = Flask(__name__)

    return flask_app