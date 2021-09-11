import datetime
from app.exception import WrongResource

class ChildService:
    def __init__(self, child_dao):
        self.child_dao = child_dao

    def save_measured_datas(self, measured_datas, child_id):
        if(self.child_dao.find_child_id(child_id)):
            now = datetime.datetime.now()

            measured_datas['measured_time'] = now.strftime('%H:%M:%S')
            measured_datas['child_id'] = child_id

            response = self.child_dao.insert_measured_datas(measured_datas)
        
            return response
        else:
            return WrongResource()