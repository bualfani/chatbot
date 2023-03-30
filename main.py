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

@app.route('/', methods=['POST'])
def webhook():
    # Parse webhook data
    data = request.get_json()
    if data['object'] == 'page':
        for entry in data['entry']:
            for messaging_event in entry['messaging']:
                if messaging_event.get('message'):
                    # Handle message
                    sender_id = messaging_event['sender']['id']
                    recipient_id = messaging_event['recipient']['id']
                    message_text = messaging_event['message']['text']
                    send_message(sender_id, "Hello! I am a chatbot built using the Facebook API.")

    return "ok", 200