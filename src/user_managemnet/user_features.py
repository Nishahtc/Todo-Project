from  src.user_managemnet.user_manage import UserManage
from src.utility.validation import *
from src.utility.check_user import check_user


class UserFeature():
    user_manage = UserManage()
    
    def signup(self):
        try:
            name = validate_name(input("Enter your name : "))
            if(not name):
                raise Exception("please enter valid name.")
            
            email = validate_email(input("Enter your email : "))
            if(not email):
                raise Exception("please enter valid email.")
            
            password = validate_password(input("Enter New  password : "))
            if(not password):
                raise Exception(input("please enter valid password should have a symbol, digit, upper and lower charactor."))

            role = validate_role(input("Enter role : "))
            if(not role):
                raise Exception("please enter a valid role.")
            
            user_manage.UserManage user_signup(name,email,password,role)
        except Exception as error:
            print(error)   
            

    def login(self):
        try:
            email = validate_email(input("Enter email : "))
            if(not email):
                raise Exception("Please enter valid email.")
            if(not check_user(email)):
                raise Exception("user not exist with this email.")
            
            password = validate_password(input("Enter password : "))
            if(not password):
                raise Exception("Please enter valid password.")
            print("before")
            self.user_login(email,password)
            print("after")
        except Exception as error:
            print(error)   

            


            
            
           
            

            
        
    
