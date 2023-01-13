from twilio.rest import Client

# Twilio account informaiton
account_sid = "AC25f5cabe9a73f1698db05d17d6d70cb8"
auth_token = "cc880c6be70c725b4ccaec32aa455edb"

client = Client(account_sid, auth_token)

message = client.api.account.messages.create(
		to="+16085152930",
		from_="+16505823628",
		body="This is a test text message")
