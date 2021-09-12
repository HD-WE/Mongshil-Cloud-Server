from flask import Blueprint, request
from flask.globals import session

from app.exception import NotAllowedMethod, Unauthorized, WrongResource

def parents_view(parents_service):
    parents_blueprint = Blueprint('parents', __name__, url_prefix='/parents')

    @parents_blueprint.route('/', methods=['GET'])
    def get_parents_info():
        if request.method == 'GET':
            try:
                parents_code = session.get('parents_code', None)

                response = parents_service.get_parents_info(parents_code)

                return response
            except:
                return Unauthorized()
        else:
            return NotAllowedMethod()

    @parents_blueprint.route('/childs', methods=['GET'])
    def get_child_info():
        if request.method == 'GET':
            session['parents_code'] = "BBB"
            try:
                parents_code = session.get('parents_code', None)
                response = parents_service.get_child_info(parents_code)

                return response
            except:
                return WrongResource()
        else:
            return NotAllowedMethod()

    return  parents_blueprint