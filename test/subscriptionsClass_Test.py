from roamPy.roamClass import Roam
import unittest

class Test_subscriptions(unittest.TestCase):

    with open('C:/Users/maahutch/dataIndexApi/roamKey.txt') as f: 
        token = f.readlines()

    roam = Roam(url='https://api.roam.plus/external/', token = token[0])


    def testGetAllSubscriptions(self, roam=roam):
        result = roam.getAllSubscriptions()
        self.assertIsInstance(result, list)

    def testGetOneSubscription(self, roam=roam):
        result = roam.getOneSubscription('294')
        self.assertIsInstance(result, dict)

    def testGetOneSubwithRelations(self, roam=roam):
        result = roam.getOneSubwithRelations('294', ['product', 'subscriptionPeriods', 
                                                     'notes', 'links', 'files', 
                                                     'licensePeriods.license.publisher',
                                                     'licensePeriods.licensePeriodStatus'])
        self.assertIsInstance(result, dict)

if __name__ == '__main__':
    unittest.main()