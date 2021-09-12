import datetime
from flask import json

from flask.json import jsonify
from sqlalchemy.sql.expression import false, true
from app.exception import WrongResource

class ChildService:
    def __init__(self, child_dao):
        self.child_dao = child_dao

    def save_measured_datas(self, measured_datas, child_id):
        if(self.child_dao.find_child_id(child_id) != 0):
            if(self.check_is_weared(measured_datas) == true):
                now = datetime.datetime.now()

                print(measured_datas)

                measured_datas['measured_time'] = now.strftime('%H:%M:%S')
                measured_datas['child_id'] = child_id

                response = self.child_dao.insert_measured_datas(measured_datas)
            
                return response
            else:
                return jsonify({"message" : "child is not weared device"})
        else:
            return WrongResource()

    def get_temperature(self, child_id):
        if(self.child_dao.find_child_id(child_id) != 0):
            response = self.child_dao.select_temperature(child_id)

            return jsonify({"temperature" : response})
        else:
            return WrongResource()

    def get_heart_rate(self, child_id):
        if(self.child_dao.find_child_id(child_id) != 0):
            response = self.child_dao.select_heart_rate(child_id)

            return jsonify({"heart_rate" : response})
        else:
            return WrongResource()

    def get_movement(self, child_id):
        if(self.child_dao.find_child_id(child_id) != 0):
            response = self.child_dao.select_movement(child_id)

            return jsonify({"movement" : response})
        else:
            return WrongResource()

    def get_measured_time(self, child_id):
        if(self.child_dao.find_child_id(child_id) != 0):
            response = self.child_dao.select_measured_time(child_id)

            return jsonify({"measured_time" : str(response)})
        else:
            return WrongResource()

    def get_is_weared(self, child_id):
        if(self.child_dao.find_child_id(child_id) != 0):
            response = self.child_dao.select_is_weared(child_id)

            if(response == 1): response = "true"
            else: response = "false"

            return jsonify({"is_weared" : response})
        else:
            return WrongResource()

    def check_is_weared(self, measured_datas):
        if(float(measured_datas['temperature']) < 20 or int(measured_datas['heart_rate']) < 20):
            return false
        else:
            return true