from flask import session
from flask_restful import Resource

class LogoutChild(Resource):
    def get(self):
        session.pop('child_id', None)
        return "logout success", 200

class LogoutParents(Resource):
    def get(self):
        print(session['parents_code'])
        session.pop('parents_code', None)
        return "log out success", 200