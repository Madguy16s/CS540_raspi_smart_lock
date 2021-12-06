Project Summary
---------------
This is an RFID Smart Lock Project. When a valid RFID card is scanned 
the user will be prompted to enter a password. This password is specific
to the card. If the corrsct passwrod is entered, the lock will unlock
for 2 seconds. If the password is incorrect the user will be prompted
that they have, "Wrong credentials" and can scan another RFID card to
try again.

Files (Written in Python 3)
---------------
  - smart_lock.py
  - write.py

Equipment Needed
---------------
  - 5V Solenoid Lock 
  - Jumper Wires
  - Raspbery Pi 

Instructions
---------------
1. Setup
	First you must get the RFID card's unique ID. To do so run 
	'read.py' and scan your RFID card. The screen should print
	your card's unique ID along with any texted stored on the 
	card, if there is any. (A blank card probbaly won't have 
	any text stored.) Copy or Save your card's unique ID. 
	
	Next, open 'smart_lock.py'. Add your card's unique ID to
	the dictionary on line 11 along with a String password of
	your choosing. Notice, we used a 3 digit number but 
	did so in String format and NOT integer format. 

2. Running 'smart_lock.py'
	You are now ready to use your smart lock. Simply, run
	'smart_lock.py' by entering 'python3 smart_lock.py' on your terminal and scan your RFID card. You'll then be 
	prompted to "Input your password:". Enter your password 
	that you inserted into the dictionary on line 11. If the 
	scanned card's unique ID is in the Dictionary on Line 11
	AND the card's ID maps to the password entered the lock 
	will unlock. You'll then be prompted with 
	"entry validated, lock is unlocked for 2 seconds". The lock 
	will remain unlocked for 2 seconds and then lock again. At
	this point, the program will stop running. 

	If the wrong credentials are entered the program will continue
	to run until the correct credentials are entered. 

