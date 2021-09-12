import json

from flask import session
from flask import json
from flask.json import jsonify

from app.exception import WrongResource

class ParentsService():
    def __init__(self, parents_dao):
        self.parents_dao = parents_dao

    def get_parents_info(self, parents_code):
        if(self.parents_dao.find_parent_code(parents_code) != 0):

            response = self.parents_dao.select_parents_info(parents_code)

            return jsonify({"name" : response['name'], 
                            "parents_code" : response['parents_code']})
        else:
            return WrongResource()

    def get_child_info(self, parents_code):
        if(self.parents_dao.find_parent_code(parents_code) != 0):
            response = self.parents_dao.select_child_info(parents_code)

            dict_list_1 = []
            key = ["name", "device_id"]

            for i in range(len(response)):
                dict_list_1.append(dict(zip(key, response[i])))
            
            json.dumps(dict_list_1)

            return jsonify(dict_list_1)
        else:
            return WrongResource()
