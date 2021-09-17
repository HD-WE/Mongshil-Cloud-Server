from flask import request, session
from flask_restful import Resource

from app.model.child.child import Child
from app.model.parents.parents import Parents

class LoginChild(Resource):
    def post(self):
        account = request.json
        
        response = Child.get_child_for_login(account['parents_code'], account['name'])

        session['child_id'] = response.id

        return "login success", 200

class LoginParents(Resource):
    def post(self):
        account = request.json

        response = Parents.get_parents_for_login(account['email'], account['password'])

        session['parents_code'] = response.parents_code

        return "login success", 200

