from flask import request
from flask.json import jsonify
from flask_restful import Resource
from flask_mail import Mail, Message
from server import app
import random

# class Child:

class ParentsRegister(Resource):
    def get(self):
        return jsonify({"message" : "testing"})

    def post(self):
        Parent_register = request.json['email']
       
        mail = Mail(app)

        app.config['MAIL_SERVER'] = 'smtp.gmail.com'
        app.config['MAIL_PORT'] = 465
        app.config['MAIL_USERNAME'] = 'mungshilcloud@gmail.com'
        app.config['MAIL_PASSWORD'] = 'andtlfrnfma!'
        app.config['MAIL_USE_TLS'] = False
        app.config['MAIL_USE_SSL'] = True

        rand_code = random.randrange(100000, 999999)
        rand_code = str(rand_code)

        mail_reciever = Parent_register
        title = 'Mungshil Cloud Email Verification Code: {}'.format(rand_code)
        msg = Message(title, sender='mungshilcloud@gmail.com', recipients=[mail_reciever])

        msg.html="""
                <img src="https://avatars.githubusercontent.com/u/86836065?s=40&v=4">
                <h1 style=" font: italic">Welcome<h1>
             """
        mail.send(msg) 
        return jsonify({"message" : "send email success"})