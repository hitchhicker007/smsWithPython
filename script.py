from twilio.rest import Client
from data import sid,my_cell, token, my_twillio

# Find these values at https://twilio.com/user/account
client = Client(sid, token)

my_msg = "this is hitch hicker's project..."

message = client.messages.create(to=my_cell, from_=my_twillio,
                                     body=my_msg)