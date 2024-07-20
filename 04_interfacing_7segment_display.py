'''Exp 4: Interfacing 7-segment Display with Raspberry Pi

You need to connect a 7-segment display and a button to Raspberry Pi. 
The display should show the number of times the button is pressed. 
The initial count shown in the display should be 0. On button presses, 
the count goes from 1 to 9 and then again to 0, 1 ... 9 and repeats.

To prepare before coming for the lab:
* Pins of the 7-segment display and their connections
* Code for interfacing the display with RPi

Note:
There are 2 types of 7-segment display - common anode, common cathode. 
Both the types are available in our lab. 
Study how the code is different for the 2 types.

https://microdigisoft.com/7-segment-display-interfacing-with-raspberry-pi/
'''

from RPI import GPIO
from gpiozero import Button
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(2,GPIO.OUT)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(9,GPIO.OUT)

digits=[[0,0,0,0,0,0,1],
        [1,0,0,1,1,1,1],
        [0,0,1,0,0,1,0],
        [0,0,0,0,1,1,0],
        [1,0,0,1,1,0,0],
        [0,1,0,0,1,0,0],
        [0,1,0,0,0,0,0],
        [0,0,0,1,1,1,1],
        [0,0,0,0,0,0,0],
        [0,0,0,1,0,0,0]]

pins=[17,27,9,21,22,3,2]

def hello():
    for j in range(0,7):
        if(digits[hello.x[j]==0]):
            GPIO.output(pins[j],GPIO.LOW)
        else:
            GPIO.output(pins[j],GPIO.HIGH)
        hello.x=(hello.x+1)%10
hello.x=0
test=Button(26)
test.when_pressed=hello


'''
from RPI import GPIO
import time
import os, sys

GPIO.setwarnings(False)
GPIO.setmode(BCM)
gpin =[17,27,9,21,22,3,2]
for i in gpin:
    GPIO.setup(i,GPIO.OUT)
    
digitclr=[1,1,1,1,1,1,1]
digit0=[0,0,0,0,0,0,1]
digit1=[1,0,0,1,1,1,1]
digit2=[0,0,1,0,0,1,0]
digit3=[0,0,0,0,1,1,0]
digit4=[1,0,0,1,1,0,0]
digit5=[0,1,0,0,1,0,0]
digit6=[0,1,0,0,0,0,0,]
digit7=[0,0,0,1,1,1,1]
digit8=[0,0,0,0,0,0,0]
digit9=[0,0,0,1,1,0,0,]

def digdisp(digit):
   for x in range (0,7):
     GPIO.output(gpin[x], digitclr[x])
   for x in range (0,7):
     GPIO.output(gpin[x], digit[x])
     
#routine to display digit from 0 to 9
digdisp(digit0)
time.sleep(1)
digdisp(digit1)
time.sleep(1)
digdisp(digit2)
time.sleep(1)
digdisp(digit3)
time.sleep(1)
digdisp(digit4)
time.sleep(1)
digdisp(digit5)
time.sleep(1)
digdisp(digit6)
time.sleep(1)
digdisp(digit7)
time.sleep(1)
digdisp(digit8)
time.sleep(1)
digdisp(digit9)
time.sleep(1)
'''
