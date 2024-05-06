#pattern using LED's
from time import sleep
from RPi import GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pin1=8
pin2=12
pin3=17

GPIO.setup(pin1,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(pin2,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(pin3,GPIO.OUT,initial=GPIO.LOW)

while True:
    GPIO.output(pin1,GPIO.HIGH)
    sleep(1)
    GPIO.output(pin2,GPIO.HIGH)
    sleep(1)
    GPIO.output(pin3,GPIO.HIGH)
    sleep(1)
    GPIO.output(pin1,GPIO.LOW)
    sleep(1)
    GPIO.output(pin2,GPIO.LOW)
    sleep(1)
    GPIO.output(pin3,GPIO.LOW)
    sleep(1)
    
    
'''
from time import sleep
from RPI import GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwraning(False)
GPIO.setup(pin, GPIO.PUT, initial=GPIO.LOW)
GPIO.output(pin, GPIO.HIGH)
GPIO.output(pin, GPIO.LOW)
'''
