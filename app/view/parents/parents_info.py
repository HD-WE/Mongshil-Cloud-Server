from flask.globals import session
from flask_restful import Resource
from flask import jsonify, session, request

from app.model.parents.parents import Parents
from app.exception import Unauthorized

class ParentsInfo(Resource):
    def get(self):
        try:
            parents_code = session['parents_code']
        except:
            raise Unauthorized()

        parents_info = Parents.get_parents_info(parents_code)

        return jsonify({"name" : parents_info.name,
                        "parents_code" : parents_info.parents_code})

class ChangeInfo(Resource):
    def put(self):
        try:
            parents_code = session['parents_code']
        except:
            raise Unauthorized()

        json_info = request.json

        Parents.update_parents_info(parents_code, json_info['name'])

        return "success change parents info", 201