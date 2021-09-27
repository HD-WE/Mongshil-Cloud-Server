from re import M
from flask_restful import Resource
from flask import jsonify, request
import datetime
import uuid

from app.model.child.measured_data import MeasuredData
from app.exception import SuccessRequest

class Temperature(Resource):
    def get(self, child_id):
        measured_datas = MeasuredData.get_measured_datas(child_id)

        response = {"temperature" : measured_datas.temperature}
        
        return jsonify(response)

class HeartRate(Resource):
    def get(self, child_id):
        measured_datas = MeasuredData.get_measured_datas(child_id)

        response = {"heart_rate" : measured_datas.heart_rate}
        
        return jsonify(response)

class Movement(Resource):
    def get(self, child_id):
        measured_datas = MeasuredData.get_measured_datas(child_id)

        response = {"movement" : measured_datas.movement}

        return jsonify(response)

class MeasuredTime(Resource):
    def get(self, child_id):
        measured_datas = MeasuredData.get_measured_datas(child_id)

        response = {"measured_time" : measured_datas.measured_time}

        return jsonify(response)

class MeasuredDatas(Resource):
    def post(self, child_id):  
        measured_datas = request.json

        id = str(uuid.uuid1()).replace("-", "")[0:12]
        now = datetime.datetime.now()

        measured_datas['measured_time'] = now

        MeasuredData.insert_measured_datas(child_id, id, measured_datas)

        return "", 201
