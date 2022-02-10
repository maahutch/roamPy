from roamPy.heartbeatClass import heartbeat
from roamPy.subscriptionsClass import subscriptions
from roamPy.subscriptionPeriodsClass import subscriptionPeriod
from roamPy.productsClass import products
from roamPy.licensesClass import license

class Roam(heartbeat, subscriptions, subscriptionPeriod, products, license):

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

    


        
        




