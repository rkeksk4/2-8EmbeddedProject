import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

def init(port):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(port, GPIO.OUT)

def buzz(port,pitch,duration):
    period=1.0/pitch
    delay=period/2
    cycles=int(duration*pitch)
    for i in range(cycles):
        GPIO.output(port,True)
        time.sleep(delay)
        GPIO.output(port,False)
        time.sleep(delay)

def LEDon(port):
    GPIO.output(port,True)

def LEDoff(port):
    GPIO.output(port,False)