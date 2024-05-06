'''Exp 8: Interfacing Camera with Raspberry Pi
Connect a camera with Raspberry Pi and write a program to take a picture and a video. 
Use the picamera library to adjust the brightness, contrast, resolution of the picture and apply image effects.
https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/7
'''

from picamera import PiCamera
import time

camera = PiCamera()
time.sleep(2)
camera.resolution = (1280, 720)
camera.vflip = True
camera.contrast = 10
camera.brightness = 60
camera.image_effect = "watercolor"

file_name = "/home/pi/Pictures/img_" + str(time.time()) + ".jpg"
print("cheese")
time.sleep(3)
camera.capture(file_name)
print("Done.")

file_name = "/home/pi/Pictures/video_" + str(time.time()) + ".h264"
time.sleep(3)
print("Start recording...")
camera.start_recording(file_name)
camera.wait_recording(5)
camera.stop_recor
print("Done.")