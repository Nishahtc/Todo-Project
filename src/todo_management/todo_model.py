



class TodoModel:
    def __init__(self,id,task,user):
        self.id=id
        self.task=task
        self.user = user


    def __str__(self):
        return {"id":{self.id},"task":{self.task},"user":{self.user}}
    

         
