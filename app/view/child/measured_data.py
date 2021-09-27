from re import M
from flask_restful import Resource
from flask import jsonify, request
import datetime
import uuid

from app.model.child.measured_data import MeasuredData

class MeasuredDatas(Resource):
    def post(self, child_id):  
        json_request = request.json

        measured_datas = {}
        pasing_json = []

        start_index = 1
        spot_index = 0

        id = str(uuid.uuid1()).replace("-", "")
        now = datetime.datetime.now()

        for i in range(len(json_request['measured_data'])):
            if json_request['measured_data'][i] == ',' or json_request['measured_data'][i] == '@':
                spot_index = i
                pasing_json.append(json_request['measured_data'][start_index:spot_index])
                start_index = i + 1

        if int(pasing_json[2]) > 150 or int(pasing_json[3]) > 150 or int(pasing_json[4]) > 150:
            measured_datas['movement'] = "strong"
        else:
            measured_datas['movement'] = "weak"

        measured_datas['measured_time'] = now
        measured_datas['temperature'] = pasing_json[0]
        measured_datas['heart_rate'] = pasing_json[1]
        measured_datas['location'] = json_request['location']

        MeasuredData.insert_measured_datas(child_id, id, measured_datas)

        return "success save measured datas", 201
