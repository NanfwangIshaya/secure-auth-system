from auth import hash_password, verify_password
from database import load_users, save_users
from logger import log_event


MAX_ATTEMPTS = 3
attempts = {}


def register():
    users = load_users()

    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in users:
        print("User already exists!")
        return

    users[username] = hash_password(password)
    save_users(users)

    log_event(f"REGISTERED: {username}")

    print("Registration successful!")


def login():
    users = load_users()

    username = input("Enter username: ")
    password = input("Enter password: ")

    if username not in users:
        print("User not found!")
        log_event(f"UNKNOWN USER: {username}")
        return

    if username not in attempts:
        attempts[username] = 0

    if attempts[username] >= MAX_ATTEMPTS:
        print("Account locked!")
        log_event(f"LOCKED ACCOUNT: {username}")
        return

    if verify_password(users[username], password):
        print("Login successful!")
        log_event(f"SUCCESS LOGIN: {username}")
        attempts[username] = 0
    else:
        attempts[username] += 1
        print("Wrong password!")
        log_event(f"FAILED LOGIN: {username}")


def main():
    while True:
        print("\n==== Secure Authentication System ====")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option")


main()