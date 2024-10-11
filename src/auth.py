from src.user_managemnet.user_features import UserFeature

def auth():



    while True:
        print("1.login")
        print("2.signup")
        print("3.exit")

        choice = input("please choose any option : ")
        if(choice == "1"):
            UserFeature().login()
        elif(choice == "2"):
            UserFeature().signup()
        elif(choice == "3"):
            break
        else:
            print("please choose rigth option.")
            
            
            


