from app.extension import db
from app.model.mixin import BaseMixin
from app.exception import WrongResource

class Parents(db.Model, BaseMixin):
    __tablename__ = 'user'

    parents_code = db.Column(db.String(45), primary_key=True)
    email = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(15), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False)

    def __init__(self, parents_code, email, name, password, created_at):
        self.parents_code = parents_code
        self.email = email
        self.name = name
        self.password = password
        self.created_at = created_at

    @staticmethod
    def get_parents_info(parents_code):
        parents_info = Parents.query.filter_by(parents_code=parents_code).first()

        if parents_info == None:
            raise WrongResource()

        return parents_info

    def update_parents_info(parents_code, name):
        parents_info = Parents.query.filter_by(parents_code=parents_code).first()

        if parents_info == None:
            raise WrongResource()

        parents_info.name = name

        db.session.commit()