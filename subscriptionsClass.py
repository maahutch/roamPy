import requests


class subscriptions(object):
        
    def __init__(self, url, header, id = 0):
        self.url = url
        self.header = header
        self.id = id

    def getAllSubscriptions(self):
        result = []
        firstPage = requests.request("GET", url = self.url, headers = self.header)
        firstPage = firstPage.json()
        next = firstPage['links']['next']
     
        while next != None:

            page = requests.request("GET", url = next, headers = self.header)
            page = page.json()

            result.append(page)
           
            try:
                next = page['links']['next']
            except: 
                next = None

        return(result)
