import datetime

class ChildService:
    def __init__(self, child_dao):
        self.child_dao = child_dao

    def save_measured_datas(self, measured_datas):
        now = datetime.datetime.now()

        measured_datas['measured_time'] = now.strftime('%H:%M:%S')

        err, code = self.child_dao.insert_measured_datas(measured_datas)
    
        return err, code