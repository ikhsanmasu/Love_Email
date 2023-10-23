from twilio.rest import Client
from random import choice

with open(file="love_text.txt") as file:
    text = file.readlines()
    love_message = choice(text)

account_sid = "YOUR SID ACCOUNT"
auth_token = "AUTHENTICATION TOKEN"
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body=love_message,
                              from_='whatsapp:YOUR TWILIO NUMBER',
                              to='whatsapp:NUMBER YOU WANT TO SEND MESSAGE'
                          )
print(message.status)

