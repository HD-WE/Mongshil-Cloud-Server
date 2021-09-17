from flask import session
from flask_restful import Resource

class LogoutChild(Resource):
    def get(self):
        session.pop('child_id', None)
        return "logout success", 200