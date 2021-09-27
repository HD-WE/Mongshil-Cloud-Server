from flask_restful import Resource
from flask import jsonify, request, session

from app.model.child.child import Child

class StandardStatus(Resource):
    def put(self):
        child_id = session['child_id']

        json_request = request.json

        measured_datas = {}
        pasing_json = []

        start_index = 1
        spot_index = 0

        for i in range(len(json_request['measured_data'])):
            if json_request['measured_data'][i] == ',' or json_request['measured_data'][i] == '@':
                spot_index = i
                pasing_json.append(json_request['measured_data'][start_index:spot_index])
                start_index = i + 1

        measured_datas['standard_temperature'] = pasing_json[0]
        measured_datas['standard_heart_rate'] = pasing_json[1]

        Child.update_standard_status(child_id, measured_datas)

        return "success change standard status", 200
