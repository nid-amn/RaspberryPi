'''Exp 10: Interfacing 16x2 LCD Display with Raspberry Pi
Connect a 16x2 LCD and display a message.
https://pimylifeup.com/raspberry-pi-lcd-16x2/
https://www.theengineeringprojects.com/2023/01/interface-lcd-16x2-with-raspberry-pi-4.html
'''
import time
import Adafriut_CharLCD as LCD
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

lcd_rs = 25
lcd_en = 24
lcd_d4 = 23
lcd_d5 = 17
lcd_d6 = 18
lcd_d7 = 22
lcd_columns = 16
lcd_rows = 2

lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6,lcd_d7,lcd_columns, lcd_rows)

lcd.message("Hello World")
time.sleep(3.0)
lcd.clear( )

lcd.message("Goodbye!!")
time.sleep(3.0)
lcd.clear( )