



class UserManage:
    def __init__(self):
        self.user = {}

    def signup(self, id, name, email, password):
        try:
            if id in self.user:
                print(f"{self.user} is alrady exist please enter different id") 

            if name in self.user:
                print(f"{self.user} is alrady exist please enter different name")
            
            if email in self.user:
                print(f"{self.user} is alrady exist please enter different email")
            
            if password in self.user:
                print(f"{self.user} is alrady exist please enter different password")
        except Exception as error:
            print(error)
            
    def login(self,name,password):
        try:
            if self.user in self.user and self.user[name]==password:
                print("Login successfully. ") 
                
            else:
                print("invalid username or password ") 
        except Exception as error:
            print(error)
                








             
        

           




           
   

    