#aim to control intensity of led using buttons
'''Exp 3: LED intensity Control using PWM in Raspberry Pi
The aim of the experiment is to control an LED using buttons. 
You need to connect 3 buttons. One button is to turn the LED on and off alternatively. 
One button is to increase the intensity of the LED – on each press, 
the LED should become brighter. Another button is to decrease the intensity of the LED.
'''
from time import sleep
from RPi import GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

light=8
buttonpin1=17
buttonpin2=15

GPIO.setup(light,GPIO.OUT)
p = GPIO.PWM(light, 100) #pulse width modulation
GPIO.setup(buttonpin1,GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(buttonpin2,GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.output(light,False)

x=0
p.start(x)
try:
    while True:
        state1 = GPIO.input(buttonpin1)
        state2 = GPIO.input(buttonpin2)
        #when button is pressed state==0
        if(state1==False): 
            x+=2
            p.ChangeDutyCycle(x)
            sleep(.1)
        elif(state2==False):
            x-=2
            p.ChangeDutyCycle(x)
            sleep(.1)
            
except KeyboardInterrupt:
    print("Keyboard interrupt detected. Exiting...") 
    
    
