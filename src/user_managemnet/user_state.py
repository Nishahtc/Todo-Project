


USER = {}

class UserState:
    def __init__(self):
        self.user = self.load_state()
       
    
    def load_state(self):
        return USER 
    

    def get_state(self):
        return self.user 
    
    def update_state(self,user):
        global USER 
        USER = user
        self.user = user
    
    



        
        
