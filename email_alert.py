import smtplib
from constants import *

def trigger_alert_email():
    try:
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(fromaddr, email_app_password)
        text = msg.as_string()
        s.sendmail(fromaddr, toaddr, text)
        print(f"You have failed to login {limit_failed_attempts} times under {time_window} seconds.")
        print("Alert email sent.")
        s.quit()
    except Exception as e:
        print("Failed to send email:", e)