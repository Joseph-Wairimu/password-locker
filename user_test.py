import unittest # Importing the unittest module
from user import user


class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = user("Joseph","kamore","kamore44","kamore44") # create user object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"Joseph")
        self.assertEqual(self.new_user.second_name,"kamore")
        self.assertEqual(self.new_user.username,"kamore44")
        self.assertEqual(self.new_user.password,"kamore44")

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(user.user_list),1)

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        user.user_list = []

    def test_save_multiple_user(self):
        '''
        test_save_multiple_contact to check if we can save multiple contact
        objects to our contact_list
        '''
        self.new_user.save_user()
        test_user = user("Test","user","chege254","chege2544") # new user
        test_user.save_user()
        self.assertEqual(len(user.user_list),2)

    def test_delete_user(self):
        '''
        test_delete_user to test if we can remove a user from our user list
        '''
        self.new_user.save_user()
        test_user = user("Test","user","chege254","chege2544") # new user
        test_user.save_user()

        self.new_user.delete_user()# Deleting a user object
        self.assertEqual(len(user.user_list),1)


if __name__ == '__main__':
    unittest.main()