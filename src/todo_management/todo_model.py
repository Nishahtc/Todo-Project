



class TodoModel:
    def __init__(self,id,task):
        self.id=id
        self.task=task

    def __str__(self):
        return {"id":{self.id},"task":{self.task}}
    

         
