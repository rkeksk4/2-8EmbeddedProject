import RPi.GPIO as GPIO
import time
import math

GPIO.setwarnings(False)
trig_port = None
echo_port = None
pulse_start = None
pulse_end = None

def init(trig, echo):
    global trig_port, echo_port
    trig_port = trig
    echo_port = echo

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(trig_port, GPIO.OUT)
    GPIO.setup(echo_port, GPIO.IN)

def getDistance():
	global trig_port, echo_port

	GPIO.output(trig_port, False)
	time.sleep(0.5)
	GPIO.output(trig_port, True)
	time.sleep(0.00001)
	GPIO.output(trig_port, False)

	while GPIO.input(echo_port) == 0 :
		pulse_start = time.time()
	while GPIO.input(echo_port) == 1 :
		pulse_end = time.time()

	distance = (pulse_end - pulse_start) * 17000
	return round(distance, 2)
  

