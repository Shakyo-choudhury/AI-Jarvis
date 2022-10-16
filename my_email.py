import smtplib
from email.message import EmailMessage
from my_inputs import talk, take_command
from my_send_email import send_email
email_list = {
    'mother': 'enter your mom\'s mail id',
}
def get_email_info():
    talk('To Whom you want to send email')
    name = take_command()
    receiver = email_list[name]
    print(receiver)
    talk('What is the subject of your email?')
    subject = take_command()
    talk('Tell me the text in your email')
    message = take_command()
    send_email(receiver, subject, message)
    talk('done boss')
if __name__==('__main__'):
    get_email_info()
    
