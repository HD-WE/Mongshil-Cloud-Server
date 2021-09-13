from flask_restful import Resource
from flask import json, jsonify, request

from app.model.child.child import Child
from app.exception import SuccessRequest

class IsWeared(Resource):
    def get(self, child_id):
        child_info = Child.get_child_info_by_child_id(child_id)

        is_weared = child_info.is_weared
        
        return jsonify({"is_weared" : is_weared})

class ParentsCode(Resource):
    def get(self, child_id):
        child_info = Child.get_child_info_by_child_id(child_id)

        parents_code = child_info.parents_code

        return jsonify({"parents_code" : parents_code})

class StandardStatus(Resource):
    def put(self, child_id):
        standard_status = request.json

        Child.update_standard_status(child_id, standard_status)

        return SuccessRequest()
