from roamPy.roamClass import Roam
import unittest


class Test_license(unittest.TestCase):

    with open('C:/Users/maahutch/dataIndexApi/roamKey.txt') as f: 
        token = f.readlines()

    roam = Roam(url='https://api.roam.plus/external/', token = token[0])


    def testGetLicenses(self, roam=roam):

        result = roam.getLicenses()
        self.assertIsInstance(result, list)

    def testGetLicensewRels(self, roam=roam):

        result = roam.getLicenseswRels(['licensePeriods', 'publisher'])
        self.assertIsInstance(result, list)

if __name__ == '__main__':
    unittest.main()