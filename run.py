from user import user
from  credentials import  credentials
import random
import string
#user details

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

def check_existing_users(username,password):
    '''
    Function that check if a user exists with that username and return a Boolean
    '''
    return user.user_exist(username,password)

def display_users():
    '''
    returns all the saved users
    '''
    return user.display_users()

#Credentials details
def create_credentials(account,username,password):
    '''
     creates  new credentials
    '''
    new_credentials = credentials(account,username,password)
    return new_credentials

def save_credentials(credentials):
    '''
    save credentials 
    '''
    credentials.save_credentials()

def delete_credentials(account) :
    """
    delete account credentials
    """ 
    return credentials.delete_credentials(account)  

def display_credentials():
    """
    display credentials
    """
    return credentials.display_credentials()


def find_by_acc(account):
    """
    find for an account
    """
    return credentials.find_by_acc(account)



    
def main():
        print("Hello Welcome to your user list. What is your name?")
        user_name = input()

        print(f"Hello {user_name}. what would you like to do?")
        print('\n')

        while True:
            print("Use these short codes : cu - create a new user, du - display users, fu -find a user, log - to login to your account, ex -exit the user list ")

            short_code = input().lower()
            if short_code == 'cu':
                    print("Create New User Account")
                    print('*'*70)
                    print("Enter your first name .....")
                    first_name = input()
                    print("Enter your last name .....")
                    second_name = input()
                    print("Enter your username .....")
                    username = input()
                    print("Enter password .....")
                    password = input()
                    save_users(create_user(first_name, second_name,username, password))
                    print('*'*70)
                    print(f"Hello {first_name}. Account created successfully. Proceed to login to access your account")
                    print('*'*70)
            elif short_code == 'log' or short_code == 'du':
                    print('*'*70)
                    print("Enter your username ...")
                    username = input()
                    print("Enter your password ...")
                    password = input()
                    if check_existing_users(username,password):
                        print("Logged in successfully")
                        while True:
                            print("Use the following short codes to check your credentials:gc -generate credentials,sc- save credentials,dp- display credentials,ex- exit")
                            print('*'*70)
                            short_code = input().lower()
                            if short_code == "sc":
                                        print ("Account name:")
                                        account = input()
                                        print("Username:")
                                        username = input()
                                        print ("Password:")
                                        password = input()
                                        save_credentials(create_credentials(account,username,password))
                                        print(f"Your {account} account details have been saved successfully.")
                                        print("-"*40)

                            elif short_code == "dp":
                                        if display_credentials():
                                           print("A list of your credentials below:")
                                           print('*'*70)
                                           for display in display_credentials():
                                            print(f"Account:{display.account} \n Username:{display.username} \n Password:{display.password}")
                                        else:
                                            print("Your credentials are not available")
                                            print("-"*20)
                            elif short_code=="ex":
                                        print("You have successfully been logged out!bye")
                                        break        
                                     
                            elif short_code =="gc":
                                        print("User")
                                        print("*"*20)

                                        print ("Username:")
                                        username = input()
                                        
                                        print ("Account:")
                                        account = input()

                                        while True:
                                            print("use short code cp- create password, allow us to generate a password for you,rp-random password")
                                            random_password = input().lower()
                                            if random_password =="cp":
                                                print("Create your password")
                                                password =input()

                                            elif random_password =="rp":    
                                                 length = int(input('\nEnter the length of password: '))
                                                 print('*'*20)
                                                 lower = string.ascii_lowercase
                                                 upper = string.ascii_uppercase
                                                 num = string.digits
                                                 symbols = string.punctuation
                                                 all = lower + upper + num + symbols  
                                                 temp = random.sample(all,length)
                                                 password = "".join(temp)               
                                                 print(f"Password has been generated successfully. Your password is{password}")

                                            break        
                                                 
                            save_credentials(create_credentials(account,username,password))
                            print('*'*20)
                    else:
                          print("please make use of the shortcodes provided.") 

            elif short_code == "ex":
                      print('*'*70)
                      print ("Thank you for interacting with our application!Bye we appreciate...")
                      break
                            
            else:
                      print('*'*70)
                      print("Invalid short codes.Try again!")
                      print('*'*70)
  
                            



if __name__ == '__main__':

    main()