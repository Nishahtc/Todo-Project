import uuid
from src.todo_management.todo_model import TodoModel
from src.todo_management.todo import Todo
from src.user_managemnet.user_state import UserState


class TodoManage(Todo):

    def add_todo(self, task):
        id = str(uuid.uuid4())[:4]
        user = UserState().get_state()
        new_todo = TodoModel(id,task,user.email)
        self.todos.append(new_todo) 
        self.save_todo()
        print(f"todo added id: {id}")
        
    def update_todo(self,id,task):
        user = UserState().get_state()
        if(user):

            if(user.role == "admin"):    
                for todo in self.todos:
                    if todo.id == id:
                        todo.task=task
                        self.save_todo()
                        print(f"Todo with ID {id} has been updated.")
                        break
                        
                else:
                    print(f"Todo with ID {id} not found.") 
            if(user.role == "user"):
                for todo in self.todos:
                    if todo.id == id and todo.user == user.email:
                        todo.task=task
                        self.save_todo()
                        print(f"Todo with ID {id} has been updated.")
                        break
                        
                else:
                    print(f"Todo with ID {id} not found.")  
              
    def delete_todo(self,id):
        user = UserState().get_state()
        if(user):
            if(user.role == "admin"):
                        
                for todo in  self.todos:
                    if todo.id == id:
                        self.todos.remove(todo)
                        self.save_todo()
                        print(f"Todo with id {id} has been deleted")
                        break
                else:
                    print(f"Todo with id {id} not found.") 
            elif(user.role == "user"):
                for todo in  self.todos:
                    if todo.id == id and todo.user == user.email:
                        self.todos.remove(todo)
                        self.save_todo()
                        print(f"Todo with id {id} has been deleted")
                        break
                else:
                    print(f"Todo with id {id} not found.") 


    def get_todo(self,id):
        user = UserState().get_state()
        if(user):
            if(user.role == "admin"):

                for todo in self.todos:
                    if todo.id == id:
                        
                        print(f"Todo with ID {id}: Task - {todo.task} user - {todo.user}")
                        break
                else:
                    print(f"Todo with id {id} not found.")  
            elif(user.role == "user"):
                for todo in self.todos:
                    if todo.id == id and todo.user == user.email:
                        
                        print(f"Todo with ID {id}: Task - {todo.task}")
                        break
                else:
                    print(f"Todo with id {id} not found.")

    def get_all_todos(self):
        user = UserState().get_state()
        if(user):
            if(user.role == "admin"):

                print(f"id : task    : user ")
                
                if len(self.todos)>0:
                    for todo in self.todos:
                        print(f"{todo.id} {todo.task} {todo.user}")
                else:
                    print("your  todo record not found.")  
            elif(user.role == "user"):
                print(f"id : task  ")
                
                if len(self.todos)>0:
                    for todo in self.todos:
                        if(todo.user == user.email):
                            print(f"{todo.id} {todo.task}")


                else:
                    print("your  todo record not found.")  
                        
            

                
          



                           
       
              
        
                
                
         
 
        
        


                

                

                

        
                    
         
         
         
            

                



 
        
       





        


        


        



    