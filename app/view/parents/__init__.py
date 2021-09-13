from app.model.child.child import Child
from flask import Blueprint, request
from flask.globals import session
from flask_restful import Api

parents_blueprint = Blueprint('parents', __name__, url_prefix='/parents')
parents_api = Api(parents_blueprint)

from .parents_info import ParentsInfo, ChildInfo

parents_api.add_resource(ParentsInfo, '/info')
parents_api.add_resource(ChildInfo, '/childs')
