from random import choice
import smtplib

with open(file="love_text.txt") as file:
    text = file.readlines()
    love_message = choice(text)

to = 'email destination@gmail.com'
outlook_user = 'your email @outlook.com'
outlook_pwd = 'your app mail password'

with smtplib.SMTP("smtp-mail.outlook.com", 587) as server:
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(outlook_user, outlook_pwd)

    header = 'To: ' + to + '\n' + 'From: ' + outlook_user + '\n' + 'Subject: Daily Love Message \n'
    msg = header + f'\n {love_message} \n\n'

    server.sendmail(outlook_user, to, msg)
