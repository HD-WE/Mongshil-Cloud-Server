from app.extension import db
from app.model.mixin import BaseMixin
from app.exception import WrongResource

class MeasuredData(db.Model, BaseMixin):
    __tablename__ = 'measured_datas'

    id = db.Column(db.String(36), primary_key=True)
    child_id = db.Column(db.String(45), db.ForeignKey('child.id', ondelete='CASCADE'), nullable=False)
    temperature = db.Column(db.Float, nullable=False)
    heart_rate = db.Column(db.Integer, nullable=False)
    movement = db.Column(db.String(45), nullable=False)
    measured_time = db.Column(db.DateTime(), nullable=False)
    location = db.Column(db.String(45), nullable=False)

    def __init__(self, id, child_id, temperature, heart_rate, movement, measured_time, location):
        self.id = id
        self.child_id = child_id
        self.temperature = temperature
        self.heart_rate = heart_rate
        self.movement = movement
        self.measured_time = measured_time
        self.location = location

    @staticmethod
    def get_measured_datas(child_id):
        meausred_datas = MeasuredData.query.filter_by(child_id=child_id).order_by(MeasuredData.measured_time).first()

        if meausred_datas == None:
            raise WrongResource()

        return meausred_datas

    @staticmethod
    def insert_measured_datas(child_id, uuid, measured_datas):
        MeasuredData(id=uuid, 
                    child_id=child_id, 
                    temperature=measured_datas['temperature'], 
                    heart_rate=measured_datas['heart_rate'], 
                    movement=measured_datas['movement'],
                    measured_time=measured_datas['measured_time'],
                    location=measured_datas['location']).save()

    