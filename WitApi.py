import os
from wit import Wit

class WitApi(object):
    def __init__(self):
        WIT_SERVER_ACCESS_TOKEN = os.environ.get('WIT_SERVER_ACCESS_TOKEN', None)
        if WIT_SERVER_ACCESS_TOKEN == None:
            try:
                import local_setting
                WIT_SERVER_ACCESS_TOKEN = local_setting.WIT_SERVER_ACCESS_TOKEN
            except:
                print("You need to add WIT SERVER ACCESS TOKEN")        
        self.client = Wit(access_token=WIT_SERVER_ACCESS_TOKEN)

    def get_bot_response(self, entity, value):
        entity = entity.lower()
        bot_response = ''
        if entity == 'technology':
            bot_response = 'We are proficient at '+value
        elif entity == 'service_type':
            bot_response = 'We are providing '+value+' services to many companies around the world'
        elif entity == 'contact_information':
            bot_response = "You can send an email to datamate.ws@gmail.com with your query."+\
                           " You can also call us at +8801731246426"
        elif entity == 'wit/bye':
            bot_response = 'Goodbye.'
        elif entity == 'wit/greetings':
            bot_response = 'Hello!'
        return bot_response

    def utilize_wit_data(self, wit_data):
        bot_responses = []
        entities = wit_data['entities']
        if len(entities)==0:
            bot_responses.append("I do not know what you are talking about.")
        for entity in entities:
            entity_data_list = entities[entity]
            for entity_data in entity_data_list:
                entity_value = entity_data["value"]
                bot_response = self.get_bot_response(entity, entity_value)
                bot_responses.append(bot_response)
        return bot_responses

    def handle_user_message(self, user_message):
        wit_data = self.client.message(user_message)
        bot_responses = self.utilize_wit_data(wit_data)
        return bot_responses

if __name__ == '__main__':
    witApi = WitApi()
    user_message = "Can you develop Python projects?"
    print(user_message)
    print(witApi.handle_user_message(user_message))
    user_message = "Can you help us to develop a web application?"
    print(user_message)
    print(witApi.handle_user_message(user_message))
    user_message = "This line has nothing."
    print(user_message)
    print(witApi.handle_user_message(user_message))
