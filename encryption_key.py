from cryptography.fernet import Fernet
import os

# Load or create a decryption key
if os.path.exists('key.key'):
    with open("key.key", "rb") as f:
        key = f.read()
else:
    key = Fernet.generate_key()
    with open("key.key", "wb") as f:
        f.write(key)

fernet = Fernet(key)
