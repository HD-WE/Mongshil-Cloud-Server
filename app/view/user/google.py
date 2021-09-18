import json
import os
import sqlite3
import uuid
import datetime

from flask_restful import Resource
from flask import redirect, request, url_for, session
from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
)
from oauthlib.oauth2 import WebApplicationClient
import requests

from app.model.parents.parents import Parents

GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID", '384169453174-nqatkf14fus5mont0737kn6rud0t15vk.apps.googleusercontent.com')
GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET", 'WUMOr5h15Ev0p8ED21tqDi2q')
GOOGLE_DISCOVERY_URL = (
    "https://accounts.google.com/.well-known/openid-configuration"
)

client = WebApplicationClient(GOOGLE_CLIENT_ID)

class Login(Resource):
    def get(self):
        session.clear()
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

        if userinfo_response.json().get("email_verified"):
            unique_id = userinfo_response.json()["sub"]
            users_email = userinfo_response.json()["email"]
            picture = userinfo_response.json()["picture"]
            users_name = userinfo_response.json()["given_name"]
        else:
            return "User email not available or not verified by Google.", 400

        if Parents.get_parents_for_google(users_email, users_name) == None:
            parents_code = str(uuid.uuid1()).replace("-", "")[0:6]
            password = str(uuid.uuid1()).replace("-", "")[0:8]
            now = datetime.datetime.now()
            Parents(parents_code, users_email, users_name, password, now).save()

        session['parents_code'] = Parents.get_parents_for_google(users_email, users_name).parents_code

        return 'google login success', 200

        


def get_google_provider_cfg():
    return requests.get(GOOGLE_DISCOVERY_URL).json()