import cv2
import numpy as np
from filters import filter
import threading
import matplotlib.pyplot as plt
array_alpha = np.array([1.25])
array_beta = np.array([-30.0])

video=cv2.VideoCapture(0)
w=int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
h=int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
forcc=cv2.VideoWriter_fourcc(*'mp4v')
video_writer=cv2.VideoWriter('colorTest.mp4',forcc,30,(w,h))
while True:
    res,frame=video.read()
    if res==False:
            break
    row,col,ch=frame.shape
    frame=cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)

    mask = frame[row//2-100:row//2+100, col//2-100:col//2+100]
    mask=cv2.add(mask,array_beta,mask)
    mask=cv2.multiply(mask,array_alpha,mask)
    # mask=cv2.equalizeHist(mask)
    # blr=filter(frame,15,1/255)
    blr=cv2.blur(frame,(35,35))
    blr[row//2-100:row//2+100, col//2-100:col//2+100]=mask
    avg=np.average(mask)
    # rm,cm=mask.shape
    # c=0
    # for i in range(rm):
    #     for j in range (cm):
    #         c+=mask[i,j]
    # c=c//(rm*cm)

    if avg<80:
        color='black'
    elif avg>=80 and avg<=180:
        color='gray'
    else:
        color='white'
    cv2.putText(blr,color,(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)
    cv2.imshow('',blr)
    blr=cv2.cvtColor(blr,cv2.COLOR_GRAY2RGB)
    video_writer.write(blr)
    if cv2.waitKey(1)==ord('q'):
        break
video.release()
video_writer.release()


