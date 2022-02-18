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