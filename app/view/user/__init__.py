from flask import Blueprint
from flask_restful import Api

user_blueprint = Blueprint('user', __name__, url_prefix='/user')
user_api = Api(user_blueprint)

from .login import LoginChild
user_api.add_resource(LoginChild, '/login_child')