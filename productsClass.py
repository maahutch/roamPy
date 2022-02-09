from requests import request

class products(object):

    def __init__(self, url, header):
        
        self.url = url 
        self.header = header


    def getAllProducts(self):
        """
        Iterates through the paginated 'Products' endpoint to return metadata 
        for all Products in the Roam instance
        
        :param self: Inherits URL and Header constructors from the Roam Class
        :return: Returns a list of json objects with metadata for all products. 
                 One list item for each page of 40 datasets from the endpoint
        """

        result = []
        urlSubs = self.url + 'products'
        firstPage = request("GET", url = urlSubs, headers = self.header)
        firstPage = firstPage.json()
        next = firstPage['links']['next']
        while next != None:
            page = request("GET", url = next, headers = self.header)
            page = page.json()

            result.append(page)
           
            try:
                next = page['links']['next']
            except: 
                next = None

        return(result)


        