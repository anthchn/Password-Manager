import bcrypt
from password_manager import *

while True:
    choice = input("Generate, manual add, view, edit admin, quit: ")

    if choice.lower() == "generate":
        while True:
            length = input("Length of password: ")
            if not length.isdigit():
                print("Please type correct value")
            else:
                length = int(length)
                password = password_generator(length)
                accept_password(password, length)
                break

    elif choice.lower() == "view":
        if login():
            option = input("Which site do you wish to see the password for? (type 'all' to view all): ")
            edit_password(option)

    elif choice.lower() == "manual add":
        manual_add(input("Purpose: "), input("Password: "))

    elif choice.lower() == "quit":
        quit()

    elif choice.lower() == "edit admin":
        if login():
            username = input("Set new admin username: ")
            password = input("Set new admin password: ")

            hashed_pass = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

            confirm = input("Are you sure you want to overwrite the admin credentials? (Y if yes): ")
            if confirm.lower() == "y":
                with open("secret.txt", "wb") as f:
                    f.write(username.encode() + b"\n")
                    f.write(hashed_pass)

                print("Admin credentials set.")
            else:
                print("Admin credentials not updated.")


    else:
        print("Invalid choice")