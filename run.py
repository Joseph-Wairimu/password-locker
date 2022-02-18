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

    def del_user(user):
        '''
        Function to delete a user
        '''
        user.delete_user()

    def find_user(username):
        '''
        Function that finds a user by username and returns the user details
        '''
        return user.find_by_username(username)

    def check_existing_users(username):
        '''
        Function that check if a user exists with that username and return a Boolean
        '''
        return user.user_exist(username)