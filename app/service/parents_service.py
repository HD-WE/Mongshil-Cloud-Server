from flask import session
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