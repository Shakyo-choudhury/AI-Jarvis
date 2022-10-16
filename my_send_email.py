import smtplib
from email.message import EmailMessage
def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
     # Make sure to give app access in your Google account
    server.login('enter your mail id', 'enter your password')
    email = EmailMessage()
    email['From'] = 'enter your mail id'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)
    
if __name__==('__main__'):
    send_email()
