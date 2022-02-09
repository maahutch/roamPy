import requests


class heartbeat(object):
        
    def __init__(self, url, header):

        self.url = url +'subscriptions'
        self.header = header
     
    def checkHeartbeat(self):
        
        response = requests.request("GET", url = self.url, headers = self.header)
        
        return(response.json())

