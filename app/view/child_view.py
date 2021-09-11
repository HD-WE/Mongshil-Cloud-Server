from flask import Blueprint, json, request, jsonify
from werkzeug.exceptions import ClientDisconnected
from app.service.child_service import ChildService
from app.exception import NotAllowedMethod

def child_view(child_service):
    child_blueprint = Blueprint('child', __name__, url_prefix='/child')

    @child_blueprint.route('/hello', methods=['GET'])
    def hello():
        #user_service = ChildService
        return "Hello"

    @child_blueprint.route('/<child_id>/measured_datas', methods=['POST'])
    def save_measured_datas(child_id):
        if request.method == 'POST':
            measured_datas_json = request.json
            
            response = child_service.save_measured_datas(measured_datas_json, child_id)

            return response
        else:
            return NotAllowedMethod()

    return child_blueprint
