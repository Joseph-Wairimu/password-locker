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

    def  test_delete_credentials(self):
        """
        tests whether credentials can be removed from the credentials_list
        """ 
        self.assertEqual(len(credentials.credentials_list),0)  
        self.new_credentials.save_credentials()
        self.assertEqual(len(credentials.credentials_list),1)
        self.new_credentials.delete_credentials() 
        