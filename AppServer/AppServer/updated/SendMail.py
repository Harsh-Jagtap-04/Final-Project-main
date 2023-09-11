import email
import smtplib
import ssl
import random
import string

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Store generated OTPs and their associated email addresses
otp_data = {}

def generate_otp(length=6):
    return ''.join(random.choices(string.digits, k=length))

def send_otp_email(receiver_email, otp):
    subject = "OTP Verification"
    body = f"Your OTP for verification is: {otp}"
    sender_email = "harshjag0401@gmail.com"
    password = "uxydxzhmslwadsya"

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    text = message.as_string()
    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, text)
        print("Email sent successfully.")
    except Exception as e:
        print("Error sending email:", str(e))

def verify_otp(email, otp):
    stored_otp = otp_data.get(email)
    if stored_otp == otp:
        return True
    return False