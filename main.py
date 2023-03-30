mport os
import sys
import json
import requests
from flask import Flask, request

app = Flask(__name__)

access_token = "<access_token>"
verify_token = "<verify_token>"

@app.route('/', methods=['GET'])
def verify():
    # Verify webhook
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == verify_token:
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200
    return "Hello world", 200

