"""
It is recommended not to write email_app_password directly into the code for security purposes.
Instead, store the application password in environment variables :
    - For Linux/macOS
        export email_app_password = 'APP_PASSWORD'
    - For Windows
        set email_app_password = APP_PASSWORD

    Then import the application password from the environment in the code :
        email_app_password = os.environ.get("EMAIL_APP_PASSWORD")

For easier, yet unsafe, execution, email_app_password is hard coded in the following.
You can create an application password for  Gmail by clicking the following link : https://myaccount.google.com/apppasswords
"""

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from pathlib import Path
import json

# Define sender and receiver E-mail address to send email in case of multiple failed login attempts
fromaddr = "SENDER_EMAIL"
toaddr = "RECEIVER_EMAIL"
email_app_password = "EMAIL_APP_PASSWORD" # prefer email_app_password = os.environ.get("EMAIL_APP_PASSWORD")

subject = "Multiple failed login attempts"
body = "Multiple failed login attempts have been detected"

# instance of MIMEMultipart
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

# Define the number of failed login attempts and the time window before sending an E-mail alert
limit_failed_attempts = 3
time_window = 30  # in seconds
storage_file = Path("timestamp.json")

if not os.path.exists("failed_attempts_file.json"):
    with open("failed_attempts_file.json", "w") as f:
        failed_attempts_file = json.dump([], f)  # write empty list to initialize file
