import requests


class subscriptions(object):
        
    def __init__(self, url, header):
        
        self.url = url 
        self.header = header
        

    def getAllSubscriptions(self):
        """
        Iterates through the paginated 'Subscriptions' endpoint to return metadata 
        for all Subscriptions in the Roam instance
        
        :param self: Inherits URL and Header constructors from the Roam Class
        :return: Returns a list of json objects with metadata for all subsriptions. 
                 One list item for each page of 40 datasets from the endpoint
        """

        result = []
        urlSubs = self.url + 'subscriptions'
        firstPage = requests.request("GET", url = urlSubs, headers = self.header)
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

    def getOneSubscription(self, id):
        """
        Exports the metadata for a single subscripion identified by its subscription ID

        :param self: Inherits URL and Header variables from Roam Class
        :param id:   A string that contains the numeric ID of the subscription
        :returns: A json object with metadata for a single subscription
        """

        urlOneSub = self.url + 'subscriptions/' + id
        
        oneSub = requests.request("GET", url = urlOneSub, headers = self.header)
        
        return(oneSub.json())
        
