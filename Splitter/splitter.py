import cv2
import numpy as np
import os
import time

# Playing video from file:
cap = cv2.VideoCapture('example.mp4')

try:
    if not os.path.exists('data'):
        os.makedirs('data')
except OSError:
    print ('Error: Creating directory of data')

currentFrame = 0
# Capture frame-by-frame
ret, frame = cap.read()

# Saves image of the current frame in jpg file
name = './data/frame' + str(currentFrame) + '.jpg'
print ('Creating...' + name)
cv2.imwrite(name, frame)
length = int(cap.get(cv2.CAP_PROP_FPS))
print(length)
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Saves image of the current frame in jpg file
    name = './data/' + str(currentFrame) + '.jpg'
    print ('Creating...' + name)
    cv2.imwrite(name, frame)
    # To stop duplicate images
    currentFrame = currentFrame + length*10 

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()



