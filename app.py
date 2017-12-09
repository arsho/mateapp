from flask import Flask, request
import requests
import json
import traceback
import random
import os

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def verify():
  if request.args.get('hub.mode' == 'subscribe' and \
                      request.args.get('hub.challenge')):
    if not request.args.get('hub.verify_token') == 'hello':
      return 'verification token mismatch', 403
    return request.args['hub.challenge'], 200
  return 'hello mate', 200

if __name__ == '__main__':
  app.run(debug=True)
