from WitApi import WitApi
witApi = WitApi()
user_message = "Do you know Python?"
responses = witApi.handle_user_message(user_message)
response = ", ".join(responses)
print(response)
