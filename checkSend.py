from twilio.rest import Client
import os
from time import sleep
from time import time

# Twilio account information and auth token
account_sid = "AC25f5cabe9a73f1698db05d17d6d70cb8"
auth_token = "cc880c6be70c725b4ccaec32aa455edb"
PHONE_SENDER = "+16505823628"
PHONE_RECIPIENT = "+16085152930"

client = Client(account_sid, auth_token)

# Caroline's phone IP 
phoneIP = "10.0.0.91"

# start off not at home
carolineStatus = 0
timeElapsed = 0
startTime = time()
currentTime = time()

checkFrequency = 10
lonelyTime = 120

# function to send text message to Caroline's phone - checks to see if the specified IP is on the network and determines if and when it should send a text
def sendText():
	print("execute sending text")
	messsage = client.api.account.messages.create(
		to=PHONE_RECIPIENT,
		from_=PHONE_SENDER,
		body="Welcome home Caroline!")

while True:
	isCarolineHome = os.system("ping -c 1 " + phoneIP)

	if isCarolineHome == 0:
		print("Caroline is home!")
		startTime = time()
		if carolineStatus == 0:
			carolineStatus = 1
			print("Trigger text!")
			sendText()
	else:
		print("Caroline is not at home")
		if timeElapsed > lonelyTime and carolineStatus == 1:
			print("Caroline is really not here!")
			carolineStatus = 0
			startTime = time()
	currentTime = time()
	timeElapsed = currentTime - startTime
	print(timeElapsed)

	sleep(checkFrequency)
