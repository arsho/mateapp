from flask import Flask, request
import requests
import json
import traceback
import random
import os, sys

webhook_verify_token = os.environ.get('webhook_verify_token', None)
app = Flask(__name__)

@app.route('/', methods = ['GET'])
def verify():
  if not request.args.get('hub.verify_token') == webhook_verify_token:
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
    return "ok", 200
  except Exception as e:
    print(str(e))

if __name__ == '__main__':
  app.run(debug=True)
