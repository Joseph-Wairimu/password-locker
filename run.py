from user import user

    def create_user(first_name,second_name,username,password):
        '''
        Function to create a new user
        '''
        new_user = user(first_name,second_name,username,password)
        return new_user

    def save_users(user):
        '''
        Function to save users
        '''
        user.save_user()