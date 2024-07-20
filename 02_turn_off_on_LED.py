#aim to control led using buttons
from time import sleep
from RPi import GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

light=8
buttonpin=17

GPIO.setup(light,GPIO.OUT)
GPIO.setup(buttonpin,GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.output(light,False)

count=0
while True:
    state = GPIO.input(buttonpin)
    if(state==False): # false if when u press the button
        if(count%2==0):
            GPIO.output(light,GPIO.HIGH)
            sleep(1)
            count=0
        else:
            GPIO.output(light,GPIO.LOW)
            sleep(1)
        count+=1
        
'''

'''
