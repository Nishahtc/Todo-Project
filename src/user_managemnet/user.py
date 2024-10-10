from src.user_managemnet.user_model import UserModel
import json
import os
USERS_FILE = "src/database/users.json"

class User:
    def __init__(self):
        self.users = self.load_users()

    def load_users(self):
        if os.path.exists(USERS_FILE):
            with open(USERS_FILE,'r')as file:
                all_users = json.load(file)
                return [UserModel(**us) for us in all_users]
        else:
            return []  
    
    def save_users(self):
        try:    
            with open(USERS_FILE,'w') as file:
                all_users = [us.__dict__ for us in self.users]
                json.dump(all_users, file, indent=4)

        except Exception as error:
            print(error)
                



       
            
                    
    