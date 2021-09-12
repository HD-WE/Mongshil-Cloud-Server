from flask import Blueprint, request
from flask.globals import session

from app.exception import NotAllowedMethod, Unauthorized

def parents_view(parents_service):
    parents_blueprint = Blueprint('parents', __name__, url_prefix='/parents')

    @parents_blueprint.route('/', methods=['GET'])
    def get_parents_info():
        if request.method == 'GET':
            if(session['parents_code'] != None):
                parents_code = session.get('parents_code', None)

                response = parents_service.get_parents_info(parents_code)

                return response
            else:
                return Unauthorized()
        else:
            return NotAllowedMethod()

    return  parents_blueprint