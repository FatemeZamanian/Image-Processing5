import cv2
import numpy as np

org=cv2.imread('lion.png',cv2.IMREAD_GRAYSCALE)
mask=np.array([[0, -1, 0], [-1, 4, -1],[0,-1,0]])
res=np.zeros((1024,1024),dtype='uint8')
rows,cols=org.shape

for i in range(1,rows-1):
    for j in range(1,cols-1):
        small_image=org[i-1:i+2,j-1:j+2]
        besco=np.multiply(small_image,mask)
        out=np.sum(besco)
        res[i,j]=out

res=cv2.resize(res,(600,600))
cv2.imshow('',res)
cv2.waitKey()