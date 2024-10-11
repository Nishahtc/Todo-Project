import uuid
from src.utility.check_user import check_user
from src.user_managemnet.user_model import UserModel
from src.user_managemnet.user import User


class UserManage(User):
    def user_signup(self, name, email, password, role):
        if(check_user(email)):
            print("Email already exist please try another email.")
        else:
            id = str(uuid.uuid4())[:10]
            new_user = UserModel(id, name, email, password, role)
            self.users.append(new_user)
            self.save_users()
            print("Signup successfully please login.")

    def user_login(self, email, password):

        """for user in self.users:
            if(user.email == email ):
                if(user.password == password):
                    print("Login successfully.")
                else:
                    print("wrong password")"""
        
        print(self.users)











        


            




            

        





       
            

            
            
    def user_login(self,name,password):
        try:
            if self.user in self.user and self.user[name]==password:
                print("Login successfully. ") 
                
            else:
                print("invalid username or password ") 
        except Exception as error:
            print(error)
                








             
        

           




           
   

    