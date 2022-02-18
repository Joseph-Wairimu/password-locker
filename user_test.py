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


if __name__ == '__main__':
    unittest.main()