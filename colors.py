import cv2
import numpy as np

def filterr(img,size,value):
    row,col=img.shape
    res=np.zeros((row,col),dtype='uint8')
    mask = np.ones((size,size),dtype='uint8')*value
    m=size//2
    n=m+1
    print(n,m)
    for i in range(m, row - m):
        for j in range(m, col - m):
            small_image = img[i - m:i + n, j - m:j + n]
            besco = np.multiply(small_image, mask)
            out = np.sum(besco)
            res[i, j] = out
    return res


video=cv2.VideoCapture(0)

while True:
    res,frame=video.read()
    if res==False:
        break
    row,col,ch=frame.shape
    frame=cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
    mask = frame[row//10:row//2, col//10:col//2]
    result=filterr(frame,15,1/255)
    result[row//10:row//2, col//10:col//2]=mask
    rm,cm=mask.shape
    c=0
    for i in range(rm):
        for j in range (cm):
            c+=mask[i,j]
    c=c//(rm*cm)
    if c<100:
        print('black')
    elif c>=100 and c<=200:
        print('gray')
    else:
        print('white')

    cv2.imshow('',result)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


