from flask.globals import request
from flask_restful import Resource
from flask import jsonify, session
import uuid

from app.model.child.child import Child
from app.exception import Unauthorized

class ChildInfo(Resource):
    def get(self):
        parents_code = session['parents_code']

        if parents_code == None:
            raise Unauthorized()

        child_info = Child.get_child_info_by_parents_code(parents_code)

        print(child_info)

        key = ["name", "device_id"]
        value = []
        info_list = []

        for i in range(len(child_info)):
            info_list.append(child_info[i].name)
            info_list.append(child_info[i].device_id)
            value.append(info_list)
        
        total_list = [dict(zip(key, value[i])) for i in range(len(child_info))]

        return jsonify({"childs" : total_list})

    def delete(self):
        parents_code = session['parents_code']

        if parents_code == None:
            raise Unauthorized()

        child_name = request.json['name']

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