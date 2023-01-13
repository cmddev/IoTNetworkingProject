import os
from time import sleep
# script to check if a specified IP address associated with a phone is on the network
phoneIP = "10.0.0.91"

while True:
	response = os.system("ping -c 1 " + phoneIP)
	if response == 0:
		print("Phone is present and online!")
	else:
		print("No phone detected!")
	sleep(2)

