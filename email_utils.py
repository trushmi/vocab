import os
import smtplib
from email.message import EmailMessage


password = os.environ['PASSWORD']
email = os.environ['EMAIL']

print("Start")

def send_email(recipients, sender):

    MyServer = smtplib.SMTP('smtp.gmail.com', 587)
    MyServer.starttls()
    MyServer.login(email, password)
    
    print("Starting to send emails: ", recipients)

    for recipient in recipients:
        msg = EmailMessage()

        msg['Subject'] = 'Time to practise vocab!'
        msg['From'] = sender
        msg['To'] = recipient["email"]
        msg.set_content(f'Hi {recipient["name"]}! This is a friendly reminder that it is time to practise your vocabulary!')
        print("Sending email to: ", recipient["email"])
        MyServer.send_message(msg)

    print("Emails sent")
    MyServer.quit()