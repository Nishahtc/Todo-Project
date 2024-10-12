import json
import os
from src.todo_management.todo_model import TodoModel
file_name="src/database/todo.json"
class Todo:
    def __init__(self):
        self.todos = self.load_todo()
    def load_todo(self):
        if os.path.exists(file_name):
            with open(file_name,'r') as f:
                all_todo = json.load(f)
                return [TodoModel(**td) for td in all_todo]
        else:
            return []
        
    def save_todo(self):
        with open(file_name, 'w') as f:
            all_todo = [td.__dict__ for td in self.todos]
            json.dump(all_todo,f,indent=4) 
               
        
           
            
        
          
                    



                
               