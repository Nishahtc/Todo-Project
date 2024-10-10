import uuid
from src.todo_management.todo_model import TodoModel
from src.todo_management.todo import Todo



class TodoManage(Todo):

    def add_todo(self, task):
        id = str(uuid.uuid4())[:4]
        new_todo = TodoModel(id,task)
        self.todos.append(new_todo) 
        self.save_todo()
        print(f"todo added id: {id}")
        
    def update_todo(self,id,task):
        for todo in self.todos:
            if todo.id == id:
                todo.task=task
                self.save_todo()
                print(f"Todo with ID {id} has been updated.")
                break
                   
        else:
            print(f"Todo with ID {id} not found.")  
              
    def delete_todo(self,id):
        for todo in  self.todos:
            if todo.id == id:
                self.todos.remove(todo)
                self.save_todo()
                print(f"Todo with id {id} has been deleted")
                break
        else:
            print(f"Todo with id {id} not found.") 

    def get_todo(self,id):
        for todo in self.todos:
            if todo.id == id:
                
                print(f"Todo with ID {id}: Task - {todo.task}")
                break
        else:
            print(f"Todo with id {id} not found.")  

    def get_all_todos(self):

        print(f"id : task  ")
        if len(self.todos)>0:
            for todo in self.todos:
                print(f"{todo.id} {todo.task}")
        else:
            print("your  todo record not found.")   
                 
            

                
          



                           
       
              
        
                
                
         
 
        
        


                

                

                

        
                    
         
         
         
            

                



 
        
       





        


        


        



    