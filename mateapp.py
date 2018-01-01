# from flask import Flask, request
# import requests
# import json
# import traceback
# import random
# import os
#
# facebook_access_token = os.environ.get('facebook_access_token', None)
# facebook_app_token = os.environ.get('facebook_app_token', None)
#
# app = Flask(__name__)
#
# token = facebook_access_token
#
# @app.route('/webhook', methods=['GET', 'POST'])
# def webhook():
#   if request.method == 'POST':
#     try:
#       data = json.loads(request.data)
#       text = data['entry'][0]['messaging'][0]['message']['text'] # Incoming Message Text
#       sender = data['entry'][0]['messaging'][0]['sender']['id'] # Sender ID
#       payload = {'recipient': {'id': sender}, 'message': {'text': "Hello World"}} # We're going to send this back
#       r = requests.post('https://graph.facebook.com/v2.6/me/messages/?access_token=' + token, json=payload) # Lets send it
#     except Exception as e:
#       print traceback.format_exc() # something went wrong
#   elif request.method == 'GET': # For the initial verification
#     if request.args.get('hub.verify_token') == facebook_app_token:
#       return request.args.get('hub.challenge')
#     return "Wrong Verify Token"
#   return "Hello from Datamate" #Not Really Necessary
#
# if __name__ == '__main__':
#   app.run(debug=True)
