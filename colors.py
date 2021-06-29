import cv2
import numpy as np
from filters import filter
import threading
import matplotlib.pyplot as plt

class color_detector(threading.Thread):
    def __init__(self):
        super(color_detector,self).__init__()
    def run(self):
        self.video=cv2.VideoCapture(0)
        while True:
            res,frame=self.video.read()
            if res==False:
                break
            row,col,ch=frame.shape
            frame=cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
            mask = frame[row//10:row//2, col//10:col//2]
            mask=cv2.equalizeHist(mask)
            result=filter(frame,15,1/255)
            result[row//10:row//2, col//10:col//2]=mask
            rm,cm=mask.shape
            c=0
            for i in range(rm):
                for j in range (cm):
                    c+=mask[i,j]
            c=c//(rm*cm)
            if c<100:
                color='black'
            elif c>=100 and c<=170:
                color='gray'
            else:
                color='white'
            cv2.putText(result,color,(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)
            cv2.imshow('',result)
            cv2.waitKey(1)

theared=color_detector()
theared.start()

