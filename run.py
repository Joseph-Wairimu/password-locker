from user import user

    def create_user(first_name,second_name,username,password):
        '''
        Function to create a new contact
        '''
        new_user = user(first_name,second_name,username,password)
        return new_user