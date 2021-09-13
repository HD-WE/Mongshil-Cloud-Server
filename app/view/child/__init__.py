from flask import Blueprint, request, jsonify
from flask_restful import Api


child_blueprint = Blueprint('child', __name__, url_prefix='/child')
child_api = Api(child_blueprint)

from app.view.child.measured_data import Temperature, HeartRate, Movement, MeasuredTime, MeasuredDatas

child_api.add_resource(Temperature, '/<child_id>/temperature')
child_api.add_resource(HeartRate, '/<child_id>/heart_rate')
child_api.add_resource(Movement, '/<child_id>/movement')
child_api.add_resource(MeasuredTime, '/<child_id>/measured_time')
child_api.add_resource(MeasuredDatas, '/<child_id>/measured_data')


from app.view.child.child_info import IsWeared, StandardStatus, ParentsCode

child_api.add_resource(IsWeared, "/<child_id>/is_weared")
child_api.add_resource(StandardStatus, "/<child_id>/standard_status")
child_api.add_resource(ParentsCode, "/<child_id>/parents_code")
