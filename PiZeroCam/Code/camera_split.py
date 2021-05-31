import picamera
import time
import os
import psutil

#HARDCODED VALUES TO CHANGE
time_lim = 20 #upper limit on total length of time to record for
length_of_segment = 5 #length of each small video in seconds

#get start time of recording and use that as filename
#record videos in increments of 10min to prevent data loss due to power off or battery depletion
#stop creating new files if space available is <0.5GB or if hardcodede time has been exceeded
start =  time.time()

print("Memory available = " + str(psutil.disk_usage('/').free/1024/1024/1024))

#keep recording until memory runs low or time_limit hasn't been reached
#create a new folder for each recording session, within which a number lists of sub-videos will be created
filename = "video at " + time.strftime("%H:%M:%S",time.localtime())
foldername = '/home/pi/Desktop/' + filename + "/"
if not os.path.exists(foldername):
    os.makedirs(foldername)
    
print("Recording: " + filename)

#write it to the file as well, for posterity
with open((foldername + "camera_log_split.txt"), "a") as file:
    file.write("\nRecording: " + filename)

with picamera.PiCamera() as camera:
    camera.resolution = (1280, 720)
    #camera.start_preview()
    for name in camera.record_sequence('%s%d_of_%d.h264' % (foldername,i,int(time_lim/length_of_segment)) for i in range(1, int(time_lim/length_of_segment)+1)):
        with open((foldername + "camera_log_split.txt"), "a") as file:
            file.write("\n\tRecording: " + name)
        print("\n\tRecording: " + name)
        camera.wait_recording(length_of_segment)

print("DONE")
print("Time Elapsed is " + str(time.time()-start) + "seconds")
