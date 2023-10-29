imgwindow = "Sorting"
import cv2
import numpy as np
from pygame import mixer

with open("video.txt", "r") as f:
    file = f.read()
    content = file.split(";")
    aud = content[1]
    video_path = content[0]

mixer.init()
mixer.music.load(aud)

def start():
    # Create a VideoCapture object and read from input file
    cv2.namedWindow(imgwindow, cv2.WINDOW_AUTOSIZE)
    cap = cv2.VideoCapture(video_path)
    mixer.music.play()
      
    # Check if camera opened successfully 
    if (cap.isOpened()== False): 
        print("Error opening video file") 
      
    while True: 
          
    # Capture frame-by-frame 
        ret, frame = cap.read() 
        if ret == True: 
        # Display the resulting frame 
            cv2.imshow(imgwindow, frame) 
              
            if cv2.waitKey(32) & 0xFF == ord('*'): 
                break
        else:
            start()
start()
