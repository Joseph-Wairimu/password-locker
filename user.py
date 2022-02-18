class user:
        """
        Class that generates new instances of user.
        """

        user_list=[] # Empty cuser list
        def __init__(self, first_name,second_name,username,password):
            '''
            __init__ method that helps us define properties for our objects.

            Args:
            first_name: New user first name.
            second_name : New user second name.
            password: New user password.
            username : New user username.
            '''
            self.first_name=first_name
            self.second_name=second_name
            self.username=username
            self.password=password
            
        def save_user(self):

            '''
            save_user method saves user objects into user_list
            '''

            user.user_list.append(self)

        def delete_user(self):

            '''
            delete_user method deletes a saved user from the user_list
            '''

            user.user_list.remove(self)

        @classmethod
        def find_by_username(cls,username):
            '''
            Method that takes in a username and returns a user that matches that username.

            Args:
                username: username to search for
            Returns :
                user details of person that matches the username.
            '''

            for user in cls.user_list:
                if user.username == username:
                 return user


        @classmethod
        def user_exist(cls,username):
            '''
            Method that checks if a user exists from the user list.
            Args:
                username: username to search if it exists
            Returns :
                Boolean: True or false depending if the user exists
            '''
            for user in cls.user_list:
                if user.username == username:
                        return True

            return False  

        def display_users(cls):
            '''
            method that returns the user list
            '''
            return cls.user_list      