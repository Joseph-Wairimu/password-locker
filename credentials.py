class credentials:
    
    """
    Class that creates new instance for credentials
    """
    credentials_list=[]#an empty credentials list
     
    def __init__(self,account,username,password):
        """
        new application and credentials are being generated
        """
        self.account=account
        self.username=username
        self.password=password




    def save_credentials(self):
        """
        save credentials in the credentials list
        """  
        credentials.credentials_list.append(self)

    def delete_credentials(self):
        """
        deletes a saved credential from the user list
        """ 
        credentials.credentials_list.remove(self)