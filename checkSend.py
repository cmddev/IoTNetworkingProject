from twilio.rest import Client
import os
from time import sleep
from time import time

# Twilio account information and auth token
account_sid = "[ACCOUNT_SID]"
auth_token = "[AUTH_TOKEN]"
PHONE_SENDER = "[SENDER_PHONE_NUMBER]"
PHONE_RECIPIENT = "[RECEIVER_PHONE_NUMBER]"

client = Client(account_sid, auth_token)

# User's phone IP 
phoneIP = "10.0.0.91"

# start off not at home
userStatus = 0
timeElapsed = 0
startTime = time()
currentTime = time()

checkFrequency = 10
lonelyTime = 120

# function to send text message to User's phone - checks to see if the specified IP is on the network and determines if and when it should send a text
def sendText():
	print("execute text")
	messsage = client.api.account.messages.create(
		to=PHONE_RECIPIENT,
		from_=PHONE_SENDER,
		body="Welcome home!")

while True:
	isUserHome = os.system("ping -c 1 " + phoneIP)

	if isUserHome == 0:
		print("User is home!")
		startTime = time()
		if userStatus == 0:
			userStatus = 1
			print("Trigger text!")
			sendText()
	else:
		print("User is not at home")
		if timeElapsed > lonelyTime and userStatus == 1:
			print("User has left home!")
			userStatus = 0
			startTime = time()
	currentTime = time()
	timeElapsed = currentTime - startTime
	print(timeElapsed)

	sleep(checkFrequency)
