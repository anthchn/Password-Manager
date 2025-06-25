# 🔐 Password Manager

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

A command-line password manager written in Python that allows to generate, store, retrieve, edit, and encrypt passwords securely. It includes admin login, email alerts for repeated failed login attempts, encryption with Fernet, and salts added to hashes.

## 📦 Features
- ✅ Strong Password Generation (random)
- 🔐 Password Encryption (Fernet symmetric encryption)
- 🧑‍💼 Admin Authentication (with bcrypt hashing)
- 🧂 Salted Hashing: Admin credentials are stored using bcrypt with automatic salt generation.
- 🛡️ Failed Login attempts Tracking with email alert after multiple attempts
- ✏️ Password Management (manual addition, view, edit, delete)
- 📧 Gmail Email Alerts using application passwords

### Skills Learned

- **Python programming**, using built in libraries.
- **Data encryption** :Understanding symmetric encryption by generating and managing cryptographic keys using `cryptography.fernet`.
- **Authentication & Access control** : Building a login system with protection against brute-force attacks via login tracking.
- **Secure password storage** : Using hashing algorithms `bcrypt` with salt for secure password storage.
- **Secure Coding Practices**
- **Email automation**, using app-specific passwords via smtplib and MIME multipart messages.


### Project Structure 

<pre> 
├── main.py                     # Main code 
├── auth.py                     # Admin login and credential management 
├── encryption_key.py           # Fernet key creation and loading 
├── password_manager.py         # Password related functions (generation, edition, etc.)
├── email_alert.py              # Alert emails sent when limit number of failed login attempts reached
├── file_ops.py                 # Tracks failed login attempts
├── constants.py                # Initial inputs for Email address, max login attempts before sending alert
├── key.key                     # Encryption key (auto-generated) 
├── passwords.txt               # Encrypted password store 
├── secret.txt                  # Admin credentials (hashed) 
├── failed_attempts_file.json   # Failed login attempts log 
├── README.md                   # Project documentation  
</pre>

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   
2. Install dependencies :
    ```bash
    pip install -r requirements.txt
 
## Usage
    python main.py 

Before executing `main.py`, user must first set `fromaddr`, `toaddr` and `email_app_password`, corresponding respectively to sender's and receiver's address, and application password of Gmail. 

The user can also modify `limit_failed_attempts` (=3 by default) and `time_window` (=10 seconds by default), corresponding respectively to the number of allowed failed login attempts and the time window under which those attempts are made before sending an email alert.

Upon first execution of `main.py`, the code prompts the user to enter admin username and password, which will be stored and hashed in the `secret.txt` file. Alongside the creation of `secret.txt`, an encryption key will be generated and stored in the `key.key` file, and `password.txt` will be created to store encrypted passwords.

The user is then prompted to choose between `Generate`, `View`, `Edit admin`, `Manual add`, `Quit` : 

- `Generate` : prompts the user to choose a password length and generate of random password of this length. The user can `accept` the password, upon which he will have to choose which `purpose` has (eg. example.com), or deny it, upon which the user can choose to rerun the password generation process or quit.

- `View` : Upon login using admin credentials, user can choose to view a single password by writing its `purpose` or choose `all` to view all existing passwords. The user can then choose to edit or delete passwords.

- `Edit admin` : Upon login using admin credentials, user can choose to change admin username and password.

- `Manual add` : prompts the user to manually enter a password and its `purpose`. 

- `Quit` : quits program.

**Note** : If `purpose` already exists, user will be asked if they want to replace it. If so, login will be needed.

**Note** : Once the `limit_failed_attempts` reached under a certain `time_window`, an email alert will be sent to the set email address in `constants.py`.

## Recommandations

Since `key.key`, `password.txt`, `secret.txt` are essential for storing and retrieving, encrypting and decrypting passwords, group policies should be set to deny delete permission, as well as modification to preserve integrity of stored data.

It is also recommended to keep a backup of all files to protect against corruption. 
