import json
import os
import sys
import requests
from flask import Flask, request, render_template, send_file

from actions import *

app = Flask(__name__)

@app.route('/', methods=['GET'])
def verify():
    # when the endpoint is registered as a webhook, it must echo back
    # the 'hub.challenge' value it receives in the query arguments
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == os.environ["VERIFY_STRING"]:
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200
    return "Oh, hello, there", 200

@app.route('/', methods=['POST'])
def callback():
    data = request.get_json()
    if data == None:
        return request.form
    if data["object"] == "page":
        for entry in data["entry"]:
            EM = EntryManager(entry)
            result_list = list(map(answer, EM.answerEntry()))
    return "OK", 200

def answer(answer_details):
    params  = {"access_token": os.environ["PAT"]}
    headers = {"Content-Type": "application/json"}
    data = JSONify(answer_details)
    if(data is None):
        return None
    r = requests.post("https://graph.facebook.com/v2.6/me/messages",params=params,headers=headers,data=data)
    if r.status_code != 200:
        print(r.status_code)
        print(r.text)

def generateQuickReplies(quick_type):
    if quick_type == 'options':
        return [
            {
                "content_type":"text",
                "title":"Help",
                "payload":"PAYLOAD_HELP"
             }
        ]
    return []

def JSONify(answer_details):
    _type = answer_details['type']
    sender_id = answer_details['sender']

    if "text" in _type:
        message_answer = answer_details['text']
        data = {
                "recipient":{"id":sender_id},
                "message":{"text":message_answer}
                }
        data['message']['quick_replies'] = generateQuickReplies("options")
        return json.dumps(data)

def log(text):
    print(str(text))
    sys.stdout.flush()
