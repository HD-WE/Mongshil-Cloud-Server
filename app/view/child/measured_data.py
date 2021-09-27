from re import M
from flask_restful import Resource
from flask import jsonify, request, session

import datetime
import uuid

from app.model.child.measured_data import MeasuredData
from app.model.child.child import Child

class MeasuredDatas(Resource):
    def post(self):  
        child_id = session['child_id']

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

        measured_datas['movement'] = check_movement(pasing_json[2], pasing_json[3], pasing_json[4])
        measured_datas['measured_time'] = now
        measured_datas['temperature'] = pasing_json[0]
        measured_datas['heart_rate'] = pasing_json[1]
        measured_datas['location'] = json_request['location']
        measured_datas['stress'] = check_stress(child_id, pasing_json[1])

        update_weared_status(child_id, pasing_json[5])

        MeasuredData.insert_measured_datas(child_id, id, measured_datas)

        return "success save measured datas", 201

def check_movement(move_x, move_y_, move_z):
    if int(move_x) > 150 or int(move_y_) > 150 or int(move_z) > 150:
        return "strong"
    else:
        return "weak"

def check_stress(child_id, heart_rate):
    child_info = Child.get_child_info_by_child_id(child_id)

    if float(heart_rate) - child_info.standard_temperature >= 20:
        return "bad"
    elif float(heart_rate) - child_info.standard_temperature > 0 and float(heart_rate) - child_info.standard_temperature < 20:
        return "nomal"
    else:
        return "relaxed"

def update_weared_status(child_id, is_weared):
    Child.update_weared_status(child_id, is_weared)