import time
import json
import random
from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        for i in range(0,100000):
            data = random.randint(0,100)
            self.send(text_data=json.dumps({
                'message':  data
            }))
            time.sleep(2)

    # def disconnect(self, close_code):
    #     pass

    # def receive(self, text_data):
    #     text_data_json = json.loads(text_data)
    #     message = text_data_json['message']
    #     for i in range(0,100000):
    #         self.send(text_data=json.dumps({
    #             'message':  random.randint(0,100)
    #         }))