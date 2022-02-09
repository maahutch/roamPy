from requests import request

class products(object):

    def __init__(self, url, header):
        
        self.url = url 
        self.header = header