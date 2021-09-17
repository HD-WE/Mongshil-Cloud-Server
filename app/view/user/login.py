from flask import request, session
from flask_restful import Resource

from app.model.child.child import Child

class LoginChild(Resource):
    def post(self):
        account = request.json
        
        response = Child.get_child_for_login(account['parents_code'], account['name'])

        session['child_id'] = response.id

        return "login success", 200