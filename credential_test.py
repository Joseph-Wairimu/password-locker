import unittest
from credentials import credentials #from credentials import class credentials

class TestCredentials(unittest.TestCase):
    def setUp(self):
        """
        setup method to run each Testcase
        """
        self.new_credentials=credentials("twitter","kamore44","kamore44")

    def test_init(self): 
        """
        test if object is initialized well
        """ 
        self.assertEqual(self.new_credentials.account,"twitter")
        self.assertEqual(self.new_credentials.username,"kamore44") 
        self.assertEqual(self.new_credentials.password,"kamore44") 
        