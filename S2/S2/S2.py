import threading
import time
import cv2

exitFlag = 0;

class myThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        
        
    def run(self):
        video_capture = cv2.VideoCapture(0)
        while True:
            got_a_frame, image = video_capture.read()
            grayimage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
            cv2.imshow('camera',grayimage)
            key = cv2.waitKey(50)
            if key == 27:
                break
        cv2.destroyWindow('camera')

# Create new threads
thread1 = myThread()

# Start new Threads
thread1.start()
thread1.join()
print ("Exiting Main Thread")
