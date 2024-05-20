import smtplib
import imghdr
from email.message import EmailMessage

PASSWORD = "PASSWORD"
SENDER = "conveniencechibatamoto@gmail.com"
RECEIVER = "conveniencechibatamoto@gmail.com

def send_email(image_path):
    email_message = EmailMessage()
    email_message["Subject"] = "Motion Detected!"
    email_message.set_content("Hey, your surveillance camera just picked up something. Take a closer look at the attached image.")

    with open(image_path, "rb") as file:
        content = file.read()
        email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    gmail.quit()
