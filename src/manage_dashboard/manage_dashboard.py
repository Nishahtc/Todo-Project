from src.user_managemnet.user_state import UserState
from src.manage_dashboard.admin_dashboard import admin_dashboard
from src.manage_dashboard.user_dashboard import user_dashboard


def manage_dashboard():
    user = UserState().get_state()
    if(user):
        if(user.role == "admin"):
            admin_dashboard()
        
        elif(user.role == "user"):
            user_dashboard()