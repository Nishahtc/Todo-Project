from src.user_managemnet.user import User



def check_user(email):
    users = User().users
    user_found = False
    for user in users:
        if user.email == email:
            user_found = True
            return True
    else:
        if(not user_found):
            return False
            

    

 


