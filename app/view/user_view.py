from flask import Blueprint
from  ..service.user_service import UserService

class UserView:
    user_blueprint = Blueprint('user', __name__, url_prefix='/user')

    @user_blueprint.route('/hello', methods=['GET'])
    def hello():
        user_service = UserService
        return user_service.hello()