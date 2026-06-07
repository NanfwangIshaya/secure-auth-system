import json
import os

USER_file = "users.json"


def load_users():
    if not os.path.exists(USER_file):
        return {}
    
    with open(USER_file, "r") as file:
        return json.load(file)
    

def save_users(users):
    with open(USER_FILE, "w") as file:
        json.dump(users, file, indent=4)