from roamPy.roamClass import Roam
import unittest

class Test_products(unittest.TestCase):

    with open('C:/Users/maahutch/dataIndexApi/roamKey.txt') as f: 
        token = f.readlines()

    roam = Roam(url='https://api.roam.plus/external/', token = token[0])


    def testGetProducts(self, roam=roam):
        result = roam.getAllProducts()
        self.assertIsInstance(result, list)


    def testGetAllProductswithPub(self, roam=roam):

        result = roam.getAllProductswithPub()
        self.assertIsInstance(result, list)



if __name__ == '__main__':
    unittest.main()