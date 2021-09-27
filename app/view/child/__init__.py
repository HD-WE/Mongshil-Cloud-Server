from flask import Blueprint, request, jsonify
from flask_restful import Api


child_blueprint = Blueprint('child', __name__, url_prefix='/child')
child_api = Api(child_blueprint)

from .measured_data import MeasuredDatas

child_api.add_resource(MeasuredDatas, '/measured_data')

from .child_info import StandardStatus

child_api.add_resource(StandardStatus, "/standard_status")

