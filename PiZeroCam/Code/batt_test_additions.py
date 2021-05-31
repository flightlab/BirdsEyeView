#Author: Bhaskar Yechuri (bhaskar.yechuri@gmail.com) - Altshuler Lab, 2021

#This script does the same as the camera_split script, but contains added functionality to stop recording and quit the program when the power regulator indicates "low battery" through one of the Pi's GPIO pins
#However, moments of high current draw can result in the power regulator spuriously outputting the "low battery" signal, resulting in the Pi quitting the program unnecessarily.
#Therefore, this feature needs a bit more testing/development, and it's best to stick with the older script to prevent unexpected behaviour

import picamera
import time
import os
import psutil
import sys

import RPi.GPIO as GPIO 



#HARDCODED VALUES TO CHANGE
low_batt_pin = 16 #tells us where the low battery pin is connected on the Rpi
time_lim = 60*60*3 #upper limit on total length of time to record for
length_of_segment = 60*10 #length of each small video in seconds



def batt_low_check(channel):
    global low_batt_pin
    global foldername
    if GPIO.input(low_batt_pin):
        print("Rising edge detected, battery is good")
        with open((foldername + "camera_log_split.txt"), "a") as file:
            file.write("\nBattery tuned high, at" + time.strftime("%H:%M:%S",time.localtime()))
            #sys.exit()
    else:
        print("Falling edge detected, battery is low")
        print("Exiting Program")
        with open((foldername + "camera_log_split.txt"), "a") as file:
            file.write("\nBattery was low, exiting program now at" + time.strftime("%H:%M:%S",time.localtime()))
            sys.exit()

GPIO.setmode(GPIO.BCM)
GPIO.setup(low_batt_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(low_batt_pin, GPIO.BOTH, callback=batt_low_check)


#get start time of recording and use that as filename
#record videos in increments of 10min to prevent data loss due to power off or battery depletion
#stop creating new files if space available is <0.5GB or if hardcodede time has been exceeded
start =  time.time()

print("Memory available = " + str(psutil.disk_usage('/').free/1024/1024/1024))

#keep recording until memory runs low or time_limit hasn't been reached
#create a new folder for each recording session, within which a number lists of sub-videos will be created
filename = "video_at_" + time.strftime("%H_%M_%S",time.localtime())
foldername = '/home/pi/Desktop/' + filename + "/"
if not os.path.exists(foldername):
    os.makedirs(foldername)

print("Recording: " + filename)
print("Battery Pin is: " + str(GPIO.input(16)))
#write it to the file as well, for posterity
with open((foldername + "camera_log_split.txt"), "a") as file:
    
    if(GPIO.input(low_batt_pin) == 0):
        file.write("Battery was low at startup, exiting program now at" + time.strftime("%H:%M:%S",time.localtime()))
        #sys.exit()
    file.write("\nRecording: " + filename)

with picamera.PiCamera() as camera:
    camera.resolution = (1280, 720)
    #camera.start_preview()
    for name in camera.record_sequence('%s%d_of_%d.h264' % (foldername,i,int(time_lim/length_of_segment)) for i in range(1, int(time_lim/length_of_segment)+1)):
        with open((foldername + "camera_log_split.txt"), "a") as file:
            file.write("at time =" + time.strftime("%H:%M:%S",time.localtime()))
            file.write("\n\tRecording: " + name)
        print("\nat time =" , time.strftime("%H:%M:%S",time.localtime()))
        print("\n\tRecording: " + name)
        camera.wait_recording(length_of_segment)

print("DONE")
print("Time Elapsed is " + str(time.time()-start) + "seconds")
