from flask import Blueprint, request
from flask.globals import session
from flask_restful import Api

user_blueprint = Blueprint('user', __name__, url_prefix='/user')
register_api = Api(user_blueprint)

from .register import ParentsRegister

register_api.add_resource(ParentsRegister, '/register')