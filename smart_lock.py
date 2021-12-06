import time
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()
pins = [18] #we toggle GPIO pin 18 to unlock the lock
GPIO.setwarnings(False)
for pin in pins:
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, GPIO.LOW)
validIDS = {52846737552: "123", 703509108240: "530"} #Dictionary withh all valid IDs and corresponding password for their card
validated = False

try:
	while not validated:
		print("Scan your RFID card: ")
		id, text = reader.read()
		password = input("Input your password: ")
		if (id in validIDs and password == validIDs[id]): # checks to make sure user used valid RFID card and input the correct password for their card
			print("entry validated, lock is unlocked for 2 seconds")
			for pin in pins:
				GPIO.output(pin, GPIO.HIGH)
				GPIO.setwarnings(False)
				validated = True
			time.sleep(2)
			print("Locked")
		else:
			print("Wrong credentials")

finally:
	GPIO.cleanup()
