'''
Exp 7: Interfacing Ultrasonic Sensor with Raspberry Pi

Aim:
Connect an ultrasonic sensor with Raspberry Pi. 
Ultrasonic sensor measures distance of objects from the sensor. 
The set up should act like a parking sensor system where if detects objects too close a red LED needs to light up. 
If objects are at a safe distance, green LED should light up. 
If an object nears the sensor, orange LED needs to light up. 
The red/yellow/green threshold distances can be set as any values.

Reference : https://pimylifeup.com/raspberry-pi-distance-sensor/
'''

import time
from RPi import GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

red = 14
yellow = 15
green = 18
pin_trig = 4
pin_echo = 17

GPIO.setup(pin_trig,GPIO.OUT)
GPIO.setup(pin_echo,GPIO.IN)
GPIO.setup(pin_trig,GPIO.LOW)

GPIO.setup(red,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(yellow,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(green,GPIO.OUT,initial=GPIO.LOW)

try:
    while True:
        GPIO.output(pin_trig,GPIO.HIGH)
        time.sleep(0.0001)
        GPIO.output(pin_trig,GPIO.LOW)
        
        while GPIO.input(pin_echo)==0:
            pulse_start= time.time()
        while GPIO.input(pin_echo)==1:
            pulse_end= time.time()
            
        duration = pulse_end-pulse_start
        distance = round(duration*17150, 2)
        print("Distance",distance,"cm")
        
        if(distance <= 20):
            GPIO.output(red, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(red,GPIO.LOW)
            
        elif(distance <= 50):
            GPIO.output(yellow, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(yellow,GPIO.LOW)
            
        else:
            GPIO.output(green, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(green,GPIO.LOW)
        
finally:
    GPIO.cleanup
    

        
        
