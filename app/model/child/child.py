from uuid import UUID
from app.exception import WrongResource
from app.extension import db
from app.model.mixin import BaseMixin

from sqlalchemy.dialects.mysql import BINARY

class Child(db.Model, BaseMixin):
    __tablename__ = 'child'

    id = db.Column(BINARY(16), primary_key=True)
    parents_code = db.Column(db.String(45),  db.ForeignKey('user.parents_code', ondelete='CASCADE'), nullable=False)
    device_id = db.Column(db.String(45), nullable=False)
    name = db.Column(db.String(45), nullable=False)
    standard_temperature = db.Column(db.Float, nullable=True)
    standard_heart_rate = db.Column(db.Integer, nullable=True)
    is_weared = db.Column(db.Boolean, nullable=False)

    def __init__(self, id, parents_code, device_id, name, standard_temperature, standard_heart_rate, is_weared):
        self.id = id
        self.parents_code = parents_code
        self.device_id = device_id
        self.name = name
        self.standard_temperature = standard_temperature
        self.standard_heart_rate = standard_heart_rate
        self.is_weared = is_weared

    @staticmethod
    def get_child_info_by_child_id(child_id):
        child_info = Child.query.filter_by(id=child_id).first()

        if child_info == None:
            raise WrongResource()

        return child_info

    @staticmethod
    def get_child_info_by_parents_code(parents_code):
        child_info = Child.query.filter_by(parents_code=parents_code).all()

        if child_info == None:
            raise WrongResource()

        return child_info

    @staticmethod
    def update_standard_status(child_id, standard_status):
        child_info = Child.query.filter_by(id=child_id).first()

        if child_info == None:
            raise WrongResource()

        child_info.standard_temperature = standard_status['standard_temperature']
        child_info.standard_heart_rate = standard_status['standard_heart_rate']

        db.session.commit()