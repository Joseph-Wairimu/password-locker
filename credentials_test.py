import unittest # Importing the unittest module
from  credentials import  credentials#from credentials import class credentials

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
   
    def test_save_credentials(self):
        """
        test whether credentials are saved in the credentials_list
        """ 
        self.new_credentials.save_credentials()
        self.assertEqual(len(credentials.credentials_list),1)


    def  test_delete_credentials(self):
        """
        tests whether credentials can be removed from the credentials_list
        """ 
        self.assertEqual(len(credentials.credentials_list),0)  
        self.new_credentials.save_credentials()
        self.assertEqual(len(credentials.credentials_list),1)
        self.new_credentials.delete_credentials() 

    def tearDown(self): 
        """
        clears up after every test is done
        """ 
        credentials.credentials_list=[] 


    def  test_find_by_account(self): 
        """
        tests whether a user can find account using account name
        """
        self.new_credentials.save_credentials()
        test_credentials = credentials("twitter","kamore44","kamore44") # new credentials 
        test_credentials.save_credentials() 
        
        found_credentials=credentials.find_by_acc("account")

    def  test_display_credentials(self):
        """
        method that displays all credentials saved by the user
        """  
        self.assertEqual(credentials.display_credentials(),credentials.credentials_list) 
        
    def test_multiple_credentials(self):
        """
        tests whether we can save multiple credentials in the credentials list
        """
        self.new_credentials.save_credentials()
        test_credentials = credentials("twitter","kamore44","kamore44")
        test_credentials.save_credentials()
        self.assertEqual(len(credentials.credentials_list),2)

                
if __name__ == '__main__':
    unittest.main()    
        