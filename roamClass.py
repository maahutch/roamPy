import requests

from heartbeatClass import heartbeat
from subscriptionsClass import subscriptions

class Roam(heartbeat, subscriptions):

    def __init__(self, url, token):
        
        self.url = url
        self.header = {
                        'Authorization': "Token " + token, 
                        'Accept': 'application/vnd.api+json' ,
                        'Accept': 'application/vnd.api+json; version=1.0'
        }

        super(Roam, self).__init__(self.url, self.header)

    def get_url(self):
        return self.url

    


        
        



