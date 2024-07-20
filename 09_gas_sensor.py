'''Exp 9: Interfacing Gas Sensor with Raspberry Pi
Connect a gas sensor (MQ2) to the Raspberry Pi and on detection of gas, 
make an LED light to come on. Use “DigitalInputDevice” module from the gpiozero library for the gas sensor.
https://www.youtube.com/watch?v=aJiD7qnklrU
'''

from gpiozero import DigitalInputDevice
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
pin = 14

GPIO.setup(pin,GPIO.out, initial = GPIO.LOW)
mq2 = DigitalInputDevice(17)

while True:
    if mq2.value == 0:
        print("Gas Detected!")
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(pin, GPIO.LOW)
    else:
        print("NA")
    time.sleep(1)

