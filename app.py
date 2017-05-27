import json
import sys
import requests
from flask import Flask, request, render_template, send_file

app = Flask(__name__)

@app.route('/', methods=['GET'])
def verify():
    # when the endpoint is registered as a webhook, it must echo back
    # the 'hub.challenge' value it receives in the query arguments
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == "veryfy_@me":
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200

@app.route('/', methods=['POST'])
def callback():
    data = request.get_json()
    if data == None:
        return request.form
    if data["object"] == "page":
        for entry in data["entry"]:
            #Do something
    return "OK", 200
