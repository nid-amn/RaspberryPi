#Logging temperature with raspberry pi
'''Exp 6: Logging Temperature Data with Raspberry Pi

Aim: You need to collect temperature and humidity values using the DHT22 sensor 
and save them in the SQLite Database every 10 seconds. 
Reference for connecting and coding temperature sensor:   https://piddlerintheroot.com/dht22/
Reference for SQLite: https://pimylifeup.com/raspberry-pi-sqlite/
'''

#sudo pip3 install adafruit-circuitpython-dht
import adafruit_dht as adf
import sqlite3
import time
import board
import RPi.GPIO as GPIO

conn = sqlite3.connect('sensor_data.db')
cur = conn.cursor()
GPIO.setwarnings(False)
cur.execute("Create table if not exists sensor_datas(timestamp Datetime,ctemp real,ftemp real,humidity real)")
conn.commit()
sensor=adf.DHT22(board.D4, use_pulseio=False)
pin = 4
GPIO.setmode(GPIO.BCM)

try:
    while True:
        humidity, ctemp=sensor.humidity,sensor.temperature
        
        if humidity is not None and ctemp is not None:
            timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
            ftemp=ctemp*(9/5)+35
            
            cur.execute("INSERT INTO sensor_datas (timestamp, ctemp, ftemp, humidity) VALUES (?,?,?,?)",(timestamp, ctemp, ftemp, humidity))
            conn.commit()
            
        else:
            print("Failed to retrieve data")
            time.sleep(10)


except KeyboardInterrupt:
    print("Interrupted")
    conn.close()
    
finally:
    print("successfully completed")
    cur.execute('Select * from sensor_datas')
    for i in cur.fetchall():
        print(i)
