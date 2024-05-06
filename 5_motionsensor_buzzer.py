'''Exp 5: Interfacing PIR sensor and Buzzer with Raspberry Pi

Aim: You need to connect a PIR (motion) sensor, 
a buzzer and an LED to RPi. On detecting motion, 
the buzzer should sound an alarm and the LED should blink.
Motion sensor: There are 2 controls for the motion sensor 
- time delay and sensitivity. 
You can experiment with adjusting them and 
checking the changes in your output.

Buzzer: To make the buzzer sound an alarm (not just a clicking sound), 
you need to use PWM. Study about that before coming for the lab.'''

import RPi.GPIO as GPIO
import time
pin=17
sensor=16
buzzer=18
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(pin,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(sensor,GPIO.IN)
GPIO.setup(buzzer,GPIO.OUT)
GPIO.output(buzzer, True) #True -> off

try:
    while(True):
        if GPIO.input(sensor):
            GPIO.output(buzzer,False)
            GPIO.output(pin,GPIO.HIGH)
            print("Motion Detected")
            while GPIO.input(sensor):
                time.sleep(0.2)
        else:
            GPIO.output(buzzer,True)
            print("No Motion")
            GPIO.output(pin,GPIO.LOW)
            time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()