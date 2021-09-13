from flask.globals import session
from flask_restful import Resource
from flask import jsonify, session, request

from app.model.parents.parents import Parents
from app.model.child.child import Child
from app.exception import  WrongResource

class ParentsInfo(Resource):
    def get(self):
        parents_code = session['parents_code']

        parents_info = Parents.get_parents_info(parents_code)

        return jsonify({"name" : parents_info.name,
                        "parents_code" : parents_info.parents_code})

class ChangeInfo(Resource):
    def put(self):
        parents_code = session['parents_code']

        json_info = request.json

        Parents.update_parents_info(parents_code, json_info['name'])

        return "", 201

class ChildInfo(Resource):
    def get(self):
        parents_code = session['parents_code']

        child_info = Child.get_child_info_by_parents_code(parents_code)

        key = ["name", "device_id"]
        value = []
        info_list = []

        for i in range(len(child_info)):
            info_list.append(child_info[i].name)
            info_list.append(child_info[i].device_id)
            value.append(info_list)
        
        total_list = [dict(zip(key, value[i])) for i in range(len(child_info))]

        return jsonify({"childs" : total_list})