from src.todo_management.todo import Todo



def check_todo(id):
    todos = Todo().todos
    todo_found = False
    for todo in todos:
        if todo.id == id:
            todo_found = True
            return True
    else:
        if(not todo_found):
            return False
       
        
            
    
    