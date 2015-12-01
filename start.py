import XboxController
import time
import sys
import os
import RPi.GPIO as GPIO

G = 27
O = 18
B = 7

threshold = 0.5
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(G, GPIO.OUT)
GPIO.setup(O, GPIO.OUT)
GPIO.setup(B, GPIO.OUT)

def setGOB(vG, vO, vB):
        GPIO.output(G, vG)
        GPIO.output(O, vO)
        GPIO.output(B, vB)

setGOB(0, 0, 0)
print "start"
def myCallBack(controlId, value):
	print "Control id = {}, Value = {}".format(controlId, value)
	if(controlId == 1 and value < -1 * threshold):
		# avance
		setGOB(0, 0, 1)
	if(controlId == 1 and value > threshold):
		# recule
		setGOB(0, 1, 0)
	if(controlId == 1 and value > -1 * threshold and value < threshold):
		# neutre joystick gauche
		setGOB(0, 0, 0)
	if(controlId == 2 and value < -1 * threshold):
		# gauche
		setGOB(0, 1, 1)
	if(controlId == 2 and value > threshold):
		# droite
		setGOB(1, 0, 0)
	if(controlId == 2 and value > -1 * threshold and value < threshold):
		# neutre joystick droit
		setGOB(1, 1, 1) 
	if(controlId == 13):
		# start
		setGOB(1, 0, 1)
	if(controlId == 12):
		# back 
		setGOB(1, 1, 0)
	if(controlId == 11):
		print "Stop"
		setGOB(0, 0, 0)
		xboxCont.stop()
		sys.exit("FIN")

xboxCont = XboxController.XboxController(
    controllerCallBack = myCallBack)

xboxCont.start()
os.system("pause")
