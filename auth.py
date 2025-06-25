import bcrypt
import os
from encryption_key import fernet
import time
from file_ops import load_failed_attempts, save_failed_attempts
from constants import time_window, limit_failed_attempts
from email_alert import trigger_alert_email

# Verify if passwords.txt and secret.txt exist, if not create them
# passwords.txt stores encrypted passwords with the generated key in key.key
if not os.path.exists("passwords.txt"):
    with open("passwords.txt", "wb") as f:
        f.write(fernet.encrypt("".encode()))

# secret.txt stores credentials to access decrypted passwords. If does not exist, create it
if not os.path.exists("secret.txt"):
    with open("secret.txt", "wb") as f:
        username = input("Set admin username: ")
        password = input("Set admin password: ")
        hashed_pass = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

        f.write(username.encode() + b"\n")
        f.write(hashed_pass)

    print("Admin credentials set.")

# Login function to access the passwords
def login():
    while True:
        username = input("Username: ")
        password = input("Password: ")
        with open("secret.txt", 'rb') as f:
            stored_user = f.readline().strip()
            stored_pass = f.readline().strip()

        if (username == stored_user.decode('utf-8')) and bcrypt.checkpw(password.encode(), stored_pass):
            print("Login Successful")
            return True

        else:
            print("Login Failed")

            #Sends time of failed login to failed_attempts_file.json to track failed login attempts
            now = time.time()
            failed_attempts = load_failed_attempts()

            # Remove attempts older than time_window
            failed_attempts = [ts for ts in failed_attempts if now - ts <= time_window]

            # Append current failed attempt timestamp
            failed_attempts.append(now)

            save_failed_attempts(failed_attempts)

            if len(failed_attempts) == limit_failed_attempts:
                trigger_alert_email()
                quit()
