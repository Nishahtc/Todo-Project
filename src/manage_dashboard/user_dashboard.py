from src.todo_management.todo_features import TodoFeature






def user_dashboard():
    todo_feature = TodoFeature()
    

    print("=================================================")
    print("1. Add task")
    print("2. Update task")
    print("3. Remove task")
    print("4. Search tasks")
    print("5. display all task")
    print("6.Exist")

    while True:
        
        choice = input("please choose  any one option (1-5): ")
        

        if choice == "1":
            todo_feature.add_task()
            continue
        
        elif choice == "2":   
            todo_feature.update_task()
            continue

        elif choice == "3":
           todo_feature.delete_task()
           continue
        
        elif choice == "4":
            todo_feature.search_todo()
            continue
        
        elif choice == "5":
           todo_feature.display_all_todo()
           continue

        elif choice == "6":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid action. Please choose a valid option from 1 to 6.")

