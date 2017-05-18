from twilio import rest

# Your Account SID from twilio.com/console
account_sid = "AC7c87e29cd0de18d62eab8c239154cb04"
# Your Auth Token from twilio.com/console
auth_token  = "06c10ee61fdc1368611e119babd6f94c"

client = rest.TwilioRestClient(account_sid, auth_token)

message = client.messages.create(
    to="+919425656165", 
    from_="+16193206991",
    body="kya ho rha??")

print(message.sid)
