from roamPy.roamClass import Roam
import unittest


class Test_roam(unittest.TestCase):

    with open('C:/Users/maahutch/dataIndexApi/roamKey.txt') as f: 
        token = f.readlines()

    roam = Roam(url='https://api.roam.plus/external/', token = token[0])

    def testGetWithURL(self, roam=roam):
        
        result = roam.getWithUrl('https://api.roam.plus/external/subscriptionPeriods/916/publisher')
        self.assertIsInstance(result, dict)