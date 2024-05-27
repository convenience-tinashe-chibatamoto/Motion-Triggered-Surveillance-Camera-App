import smtplib
import imghdr
import os
from email.message import EmailMessage

PASSWORD = os.environ['PASSWORD']
SENDER = "conveniencechibatamoto@gmail.com"
RECEIVER = "conveniencechibatamoto@gmail.com"


def send_email(image_path):
    print("send_email function started")
    email_message = EmailMessage()
    email_message["Subject"] = "Motion Detected!"
    email_message.set_content(
        "Hey, your surveillance camera just picked up something. Take a closer look at the attached image."
    )

    with open(image_path, "rb") as file:
        content = file.read()
        email_message.add_attachment(content,
                                     maintype="image",
                                     subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    gmail.quit()
    print("send_email function ended")


if __name__ == "__main__":
    send_email(image_path="images/19.png")
