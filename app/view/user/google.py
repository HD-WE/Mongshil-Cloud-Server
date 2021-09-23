import json
import os
import uuid
import datetime

from flask_restful import Resource
from flask import redirect, request, session
from flask_login import (
    current_user,
    login_required,
    login_user,
    logout_user,
)
from oauthlib.oauth2 import WebApplicationClient
import requests

from app.model.parents.parents import Parents

<<<<<<< HEAD
GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID", 'your id')
GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET", 'your secret')
=======
GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID", '["your id"]')
GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET", '[your secret]')
>>>>>>> feature/all_child_info
GOOGLE_DISCOVERY_URL = (
    "https://accounts.google.com/.well-known/openid-configuration"
)

client = WebApplicationClient(GOOGLE_CLIENT_ID)

class Login(Resource):
    def get(self):
        google_provider_cfg = get_google_provider_cfg()
        authorization_endpoint = google_provider_cfg["authorization_endpoint"]

        request_uri = client.prepare_request_uri(
            authorization_endpoint,
            redirect_uri=request.base_url + "/google",
            scope=["openid", "email", "profile"],
        )

        return redirect(request_uri)

class CallBack(Resource):
    def get(self):
        code = request.args.get("code")

        google_provider_cfg = get_google_provider_cfg()
        token_endpoint = google_provider_cfg["token_endpoint"]

        token_url, headers, body = client.prepare_token_request(
            token_endpoint,
            authorization_response=request.url,
            redirect_url=request.base_url,
            code=code,
        )
        token_response = requests.post(
            token_url,
            headers=headers,
            data=body,
            auth=(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET),
        )

        client.parse_request_body_response(json.dumps(token_response.json()))

        userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
        uri, headers, body = client.add_token(userinfo_endpoint)
        userinfo_response = requests.get(uri, headers=headers, data=body)

        userinfo_json = userinfo_response.json()
        
        if userinfo_json.get("email_verified"):
            users_email = userinfo_json["email"]
            users_name = userinfo_json["given_name"]
        else:
            return "User email not available or not verified by Google.", 400

        if Parents.get_parents_for_google(users_email, users_name) == None:
            uuid_replaced = str(uuid.uuid1()).replace("-", "")
            parents_code = uuid_replaced[0:6]
            password = uuid_replaced[0:8]
            now = datetime.datetime.now()
            Parents(parents_code, users_email, users_name, password, now).save()

        session['parents_code'] = Parents.get_parents_for_google(users_email, users_name).parents_code

        return 'google login success', 200

        
def get_google_provider_cfg():
    return requests.get(GOOGLE_DISCOVERY_URL).json()
