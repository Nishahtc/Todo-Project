import re



def validate_task(task):
    if(len(task)>0):
        return task
    else:
        return False

def validate_id(id):
    if(len(id)==4):
        return id.upper()
    else:
        return False
    
def validate_name(name):
    pattern = r'^[A-Za-z]'
    if(re.match(pattern,name)):
        return name
    else:
        return False
    

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if(re.match(pattern,email)):
        return email
    else:
        return False
    


def validate_password(password):
    pattern =r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{7,}$'
    if(re.match(pattern, password)):
        return password
    else:
        return False

def validate_role(role):
    if(role.lower()=="user" or role.lower() =="admin"):
        return role.lower()
    else:
        return False
    

    




    



        
 
    
