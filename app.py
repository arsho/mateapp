from flask import Flask, request
import requests
import json
import traceback
import random
import os, sys
from pymessenger import Bot

from WitApi import WitApi

webhook_verify_token = os.environ.get('webhook_verify_token', None)
page_token = os.environ.get('page_token', None)

bot = Bot(page_token)

app = Flask(__name__)
witApi = WitApi()

@app.route('/', methods = ['GET'])
def verify():
  if not request.args.get('hub.verify_token') == page_token:
    return 'verification token mismatch', 403
  else:
    return request.args.get('hub.challenge', 'Error shovon'), 200
  return 'hello mate', 200

@app.route('/', methods = ['POST'])
def post_message():
  try:
    data = request.get_json()
    print(data)
    sys.stdout.flush()

    if data['object'] == 'page':
      for entry in data['entry']:
        for messaging_event in entry['messaging']:

          # IDs
          sender_id = messaging_event['sender']['id']
          recipient_id = messaging_event['recipient']['id']

          if messaging_event.get('message'):
            user_message = None
            # Extracting text message
            if 'text' in messaging_event['message']:
              user_message = messaging_event['message']['text']
            else:
              user_message = 'no text'

            # Echo
            response = None
            if user_message == 'hi':
              response = 'hello'
            else:
              response = witApi.handle_user_message(user_message)
            bot.send_text_message(sender_id, response)
    
    return "ok", 200
  except Exception as e:
    print(str(e))

if __name__ == '__main__':
  app.run(debug=True)
