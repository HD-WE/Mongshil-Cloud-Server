from flask import Blueprint, json, request, jsonify
from werkzeug.exceptions import ClientDisconnected
from  ..service.child_service import ChildService

def child_view(child_service):
    child_blueprint = Blueprint('child', __name__, url_prefix='/child')

    @child_blueprint.route('/hello', methods=['GET'])
    def hello():
        #user_service = ChildService
        return "Hello"

    @child_blueprint.route('/measured_datas', methods=['POST'])
    def save_measured_datas():
        if request.method == 'POST':
            measured_datas_json = request.json
            
            err, code = child_service.save_measured_datas(measured_datas_json)

            return jsonify({"message" : err,
                            "status_code" : code})
            
        return f"{request.method} is not supported"

    return child_blueprint
