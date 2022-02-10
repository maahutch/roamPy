from roamPy.roamClass import Roam
import unittest


class Test_heartbeat(unittest.TestCase):

    with open('C:/Users/maahutch/dataIndexApi/roamKey.txt') as f: 
        token = f.readlines()

    roam = Roam(url='https://api.roam.plus/external/', token = token[0])


    def testHeartbeat(self, roam=roam):

        result = roam.checkHeartbeat()
        self.assertIsInstance(result, dict)



if __name__ == '__main__':
    unittest.main()