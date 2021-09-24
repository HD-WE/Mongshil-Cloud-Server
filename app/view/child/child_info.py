from flask_restful import Resource
from flask import json, jsonify, request

from app.model.child.child import Child
from app.exception import SuccessRequest

class StandardStatus(Resource):
    def put(self, child_id):
        standard_status = request.json

        Child.update_standard_status(child_id, standard_status)

        return "success change standard status", 200
