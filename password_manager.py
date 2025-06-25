import string
import random
from encryption_key import fernet
from auth import login

# Password generator generates a random password of length=length
def password_generator(length):
    chars = string.ascii_letters + string.digits
    password = ''.join(random.choices(chars, k=length))
    print(password)
    return password


# Encrypt the password file
def encrypt_passwords_file():
    with open("passwords.txt", "rb") as f:
        content = f.read()
    encrypted = fernet.encrypt(content)
    with open("passwords.txt", "wb") as f:
        f.write(encrypted)


def replace():
    replace = input("Usage already exists, do you wish to replace? (Y/N): ")
    if replace.lower() == "y":
        if login():
            return True

# Function to accept the generated password
# If password not accepted, asks if user wants to rerun password generation
def accept_password(password, length):
    while True:
        accept = input("Do you wish to accept password? (Y/N): ")

        if accept.lower() == "y":
            purpose = input("What is this password for: ")

            decrypted_content = ""
            try:
                with open("passwords.txt", "rb") as f:
                    decrypted_content = fernet.decrypt(f.read()).decode()
            except:
                decrypted_content = ""

            lines = decrypted_content.strip().split('\n')
            updated = False

            for i, line in enumerate(lines):
                if line.lower().startswith(purpose.lower() + " :"):
                    if replace():
                        lines[i] = f"{purpose} : {password}"
                        updated = True
                    else:
                        print("Password not saved.")
                        return
            if not updated:
                lines.append(f"{purpose} : {password}")

            updated_content = "\n".join(lines) + "\n"
            with open("passwords.txt", "wb") as f:
                f.write(fernet.encrypt(updated_content.encode()))

            print("Password saved successfully.")
            break

        elif accept.lower() == "n":
            rerun = input("Do you wish to rerun password generation? (Y/N): ")
            if rerun.lower() == "y":
                password = password_generator(length)
                accept_password(password, length)
            break

        else:
            print("Invalid input. Please enter Y or N.")

def read_passwords(option):
    try:
        with open("passwords.txt", "rb") as f:
            decrypted_content = fernet.decrypt(f.read()).decode()
    except:
        print("Failed to decrypt passwords file.")
        return None

    if option.lower() == "all":
        print("All saved passwords:\n")
        print(decrypted_content)
        return "all"
    else:
        lines = decrypted_content.strip().split('\n')
        for line in lines:
            if line.lower().startswith(option.lower() + " :"):
                print(line)
                return line
        print("No password found for this site.")
        return None


def edit_password(option):
    match = read_passwords(option)
    if not match:
        return

    # If viewing all, ask which one to edit/delete BEFORE processing
    if match == "all":
        while True:
            edit_choice = input("Do you want to edit passwords? (Y/N): ")
            if edit_choice.lower() == "y":
                option = input("Which password do you want to change/delete? (enter purpose): ").strip()

                # Re-check if the selected option exists
                try:
                    with open("passwords.txt", "rb") as f:
                        decrypted_content = fernet.decrypt(f.read()).decode()
                except:
                    print("Failed to decrypt passwords file.")
                    return

                lines_check = decrypted_content.strip().split('\n')
                found = False
                for line in lines_check:
                    if line.lower().startswith(option.lower() + " :"):
                        found = True

                if not found:
                    print(f"No password found for '{option}'.")
                    return

                break

            elif edit_choice.lower() == "n":
                return
            else:
                print("Invalid input. Please enter Y or N.")

    action = input("Action (quit, edit, delete): ").strip().lower()
    if action == "quit":
        return

    # Proceed with edit/delete
    try:
        with open("passwords.txt", "rb") as f:
            decrypted_content = fernet.decrypt(f.read()).decode()
    except:
        print("Failed to decrypt passwords file.")
        return

    lines = decrypted_content.strip().split('\n')
    new_lines = []
    updated = False

    for line in lines:
        if line.lower().startswith(option.lower() + " :"):
            if action == "delete":
                confirm = input(f"Are you sure you want to delete password for {option} ? (Y to confirm, else to cancel) : ")
                if confirm.lower() == "y":
                    print(f"Deleted password for '{option}'.")
                    updated = True
                    continue  # skip this line
                else :
                    break
            elif action == "edit":
                new_pass = input(f"Enter new password for {option}: ")
                new_lines.append(f"{option} : {new_pass}")
                updated = True
                continue
        new_lines.append(line)

    if not updated:
        print("Nothing was edited.")
        return

    updated_content = "\n".join(new_lines) + "\n"
    with open("passwords.txt", "wb") as f:
        f.write(fernet.encrypt(updated_content.encode()))

    if action == "edit":
        print("Password updated successfully.")


# Function to manually add a password
def manual_add(purpose, password):
    while True:
        decrypted_content = ""
        try:
            with open("passwords.txt", "rb") as f:
                decrypted_content = fernet.decrypt(f.read()).decode()
        except:
            decrypted_content = ""

        lines = decrypted_content.strip().split('\n')
        updated = False

        for i, line in enumerate(lines):
            if line.lower().startswith(purpose.lower() + " :"):
                if replace():
                    lines[i] = f"{purpose} : {password}"
                    updated = True
                else:
                    print("Password not saved.")
                    return

        if not updated:
            lines.append(f"{purpose} : {password}")

        updated_content = "\n".join(lines) + "\n"
        with open("passwords.txt", "wb") as f:
            f.write(fernet.encrypt(updated_content.encode()))

        print("Password saved successfully.")
        break
