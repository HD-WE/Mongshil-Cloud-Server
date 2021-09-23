from flask.globals import request
from flask_restful import Resource
from flask import jsonify, session
import uuid

from sqlalchemy.sql.operators import json_getitem_op
from sqlalchemy.sql.type_api import to_instance

from app.model.child.child import Child
from app.model.child.measured_data import MeasuredData
from app.exception import Unauthorized

class ChildInfo(Resource):
    def get(self):
        parents_code = session['parents_code']

        if parents_code == None:
            raise Unauthorized()

        child_info = Child.get_child_info_by_parents_code(parents_code)

        key = ["name"]
        value = []

        for i in range(len(child_info)):
            info_list = []
            info_list.append(child_info[i].name)
            value.append(info_list)
        
        total_list = [dict(zip(key, value[i])) for i in range(len(child_info))]

        return jsonify(total_list)

    def delete(self):
        parents_code = session['parents_code']

        if parents_code == None:
            raise Unauthorized()

        for i in range(len(request.json)):
            child_name = request.json[i]['name']
            Child.delete_child_by_parents_code(parents_code, child_name)

        return "", 200

    def post(self):
        parents_code = session['parents_code']

        if parents_code == None:
            raise Unauthorized()

        id = str(uuid.uuid1()).replace("-", "")[0:12]

        childs_info = request.json

        childs_info['id'] = id

        print(id)

        Child.add_child(parents_code, childs_info)
        
        return "", 201

class AllChild(Resource):
    def get(self):
        parents_code = session['parents_code']

        if parents_code == None:
            raise Unauthorized()

        child_info = Child.get_child_info_by_parents_code(parents_code)

        key = ["name", "is_weared", "status"]
        measured_datas_key = ["temperature", "heart_rate", "movement", "measured_time"]
        value = []

        for i in range(len(child_info)):
            child_status = MeasuredData.get_measured_datas(child_info[i].id)

            child_info_list = []
            measured_datas_list = []

            child_info_list.append(child_info[i].name)
            child_info_list.append( child_info[i].is_weared)                
            
            measured_datas_list.append(child_status.temperature)
            measured_datas_list.append(child_status.heart_rate)
            measured_datas_list.append(child_status.movement)
            measured_datas_list.append(child_status.measured_time)

            child_info_list.append(dict(zip(measured_datas_key, measured_datas_list)))
            
            value.append(child_info_list)

        
        total_list = [dict(zip(key, value[i])) for i in range(len(child_info))]

        return jsonify(total_list)