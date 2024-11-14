import smtplib
"""import os
import sys
sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            '..'
        )
    )
)"""
from bots.MongoHelper import get_single_document 

def send():
    try:
        x=smtplib.SMTP('smtp.gmail.com',587)
        x.starttls()
        conig_data=get_single_document("test_config",{"name":"email_config"},{"username":1,"password":0})
        print(config_data)
        print(config_data['username'])
        print(config_data['password'])
        x.login(config_data['username'],config_data['password'])
        # x.login("Your_email", "Your_App_Passwords")
        subject="Testing"
        body="Testing Success"
        msg="Subject:{}\n\n{}".format(subject,body)
        # x.sendmail("Sender","Receiver",msg)
        x.sendmail("sidiqfaisal30@gmail.com","mfaisalshidiq@gmail.com",msg)
        print("Successfully sent email")
    except Exception as exception:
        print(exception)
        print("Failure to send email")
    

if __name__ == "_main_":
    send()