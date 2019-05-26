import cv2
import numpy as np
import os
import time

#################### Setting up the file ################
videoFile = "videoplayback.mp4"
vidcap = cv2.VideoCapture(videoFile)
success,image = vidcap.read()

try:
    if not os.path.exists('data'):
        os.makedirs('data')
except OSError:
    print ('Error: Creating directory of data')
#################### Setting up parameters ################

seconds = 10
fps = vidcap.get(cv2.CAP_PROP_FPS) # Gets the frames per second
multiplier = fps * seconds

#################### Initiate Process ################

while success:
    frameId = int(round(vidcap.get(1))) #current frame number, rounded b/c sometimes you get frame intervals which aren't integers...this adds a little imprecision but is likely good enough
    success, image = vidcap.read()

    if frameId % multiplier == 0:
        cv2.imwrite("./data/%d.jpg" % frameId, image)

vidcap.release()
print ("Complete")