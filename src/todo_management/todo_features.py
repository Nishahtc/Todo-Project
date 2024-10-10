from src.todo_management.todo_manage import TodoManage
from src.utility.validation import *
from src.utility.check_todo import check_todo




class TodoFeature(TodoManage):
    def add_task(self):
        try:
            task = validate_task(input("Enter task : "))
            if (not task):
                 raise Exception ("you can't enter empty task.")
            self.add_todo(task)
        except Exception as e:
            print(e)

    def update_task(self):
        try:
            id = validate_id(input("Enter todo id : "))
            if(not id):
                raise Exception("please enter validate id and should be 4 length:")
            
            if(not check_todo(id)):
                raise Exception("Todo not found for given id.")
            
            task = validate_task(input("Enter todo task : "))
            if(not task):
                raise Exception("you can't enter empty task.")
            
            self.update_todo(id, task)
            
        except Exception as e:
            print(e)   

    def delete_task(self):
        try:
            id = validate_id(input("Enter todo id : "))
            if(not id):
                raise Exception("Please enter a validate id should be 4 length.")
            
            
           
            self.delete_todo(id)
        except Exception as error:
            print(error) 

    def search_todo(self):
        try:
            id = validate_id(input("Enter id for view todo : "))
            if(not id):
                raise Exception("Please enter a validate id should be 4 length.")
           
            self.get_todo(id)
        except Exception as error:
            print(error)

    def display_all_todo(self):
        try:
            
            self.get_all_todos()
        except Exception as e:
            print(e)    




            
        


            
        

        


            
        


            
            


        
        
            
        

        


            
            
        



        


             
            
            
            
            
            
                 

                



             
            
            
            
        
            

        
       
            

           
        
            
            


        

    
