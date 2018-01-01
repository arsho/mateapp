import os
from wit import Wit

try:
    import local_setting
except:
    pass

WIT_SERVER_ACCESS_TOKEN = os.environ.get('WIT_SERVER_ACCESS_TOKEN', None)

if WIT_SERVER_ACCESS_TOKEN == None:
    WIT_SERVER_ACCESS_TOKEN = local_setting.WIT_SERVER_ACCESS_TOKEN

client = Wit(access_token=WIT_SERVER_ACCESS_TOKEN)
message_text = "Can you develop Python projects?"
wit_response = client.message(message_text)
print(wit_response)