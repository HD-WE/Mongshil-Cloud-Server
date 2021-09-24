from re import M
from flask_restful import Resource
from flask import jsonify, request
import datetime
import uuid

from app.model.child.measured_data import MeasuredData

class MeasuredDatas(Resource):
    def post(self, child_id):  
        measured_datas = request.json

        id = str(uuid.uuid1()).replace("-", "")[0:12]
        now = datetime.datetime.now()

        measured_datas['measured_time'] = now

        MeasuredData.insert_measured_datas(child_id, id, measured_datas)

        return "success save measured datas", 201
