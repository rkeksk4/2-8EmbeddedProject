import RPi.GPIO as GPIO
import time
import math

GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
trig = 23
echo = 24
GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

def buzz(pitch,duration):
	period=1.0/pitch
	delay=period/2
	cycles=int(duration*pitch)
	for i in range(cycles):
		GPIO.output(21,True)
		time.sleep(delay)
		GPIO.output(21,False)
		time.sleep(delay)
 
  
print "start"

try :
	while True :
		GPIO.output(trig, False)
		time.sleep(0.5)

		GPIO.output(trig, True)
		time.sleep(0.00001)
		GPIO.output(trig, False)

		while GPIO.input(echo) == 0 :
			pulse_start = time.time()
		while GPIO.input(echo) == 1 :
			pulse_end = time.time()
 
		pulse_duration = pulse_end - pulse_start
		distance = pulse_duration * 17000
		distance = round(distance, 2)
		
		
		if(distance >= 10): 
			print "Buzzer"
			GPIO.output(20,True)
			pitch_s=10
			pitch=float(pitch_s)
	
			duration_s=1
			duration=float(duration_s)

			buzz(pitch,duration)
						
		else:
			print "No Buzzer"
			GPIO.output(20,False)
		print"Distance : ", distance, "cm"

except :
	GPIO.cleanup()

