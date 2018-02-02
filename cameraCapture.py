#/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author: wujiyang
@date: 2018-02-02
@brief: capture the camera frame by an usb camera.
'''

import cv2
import numpy as np

def getFrameFromCamera(cap):
    ret, frame = cap.read()
    # show a frame
    return frame
        

def main():
    cap = cv2.VideoCapture(0)
    while(1):
        frame = getFrameFromCamera(cap)
        cv2.putText(frame, "press 'q' to exit", (10, 30), 0, 1, (255, 0, 0), 1, False)
        cv2.imshow('capture',frame)
        if cv2.waitKey(40) & 0xFF == ord('q'):
            print 'welcome to use again, good bye~'
            break
            cv2.destroyAllWindows()
    cap.release()

if __name__ == "__main__":
    main()