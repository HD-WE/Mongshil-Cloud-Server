from flask.globals import session
from flask_restful import Resource
from flask import jsonify, session, request

from app.model.parents.parents import Parents

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