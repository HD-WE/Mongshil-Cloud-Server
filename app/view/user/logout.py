from flask import session
from flask_restful import Resource
from flask_login import logout_user

class LogoutChild(Resource):
    def get(self):
        session.pop('child_id', None)
        return "logout success", 200

class LogoutParents(Resource):
    def get(self):
        print(session['parents_code'])
        session.pop('parents_code', None)
        return "log out success", 200

class LogoutGoogle(Resource):
    def get(self):
        logout_user()
        return "log out user", 200