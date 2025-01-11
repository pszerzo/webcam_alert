import imghdr
import os
import smtplib
from email.message import EmailMessage

PW = os.getenv("PASSWORD")
SENDER = "peterszerzo@gmail.com"
def send_email(attachment):
    email_message = EmailMessage()
    email_message["Subject"] = "New movement"
    email_message.set_content("We just saw something new")

    with open(attachment, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PW)
    gmail.sendmail(SENDER, SENDER, email_message.as_string())
    gmail.quit()

    print("Email sent")


if __name__ == "__main__":
    send_email(attachment="images/4.png")