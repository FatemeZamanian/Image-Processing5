import cv2
import numpy as np

org=cv2.imread('building.tif',cv2.IMREAD_GRAYSCALE)
mask1=np.array([[-1,0,1], [-1, 0, 1],[-1,0,1]])
mask2=np.array([[-1,-1,-1], [0, 0, 0],[1,1,1]])
res1=np.zeros((600,600),dtype='uint8')
res2=np.zeros((600,600),dtype='uint8')
rows,cols=org.shape

for i in range(1,rows-1):
    for j in range(1,cols-1):
        small_image=org[i-1:i+2,j-1:j+2]
        besco1=np.multiply(small_image,mask1)
        besco2 = np.multiply(small_image, mask2)
        out1=np.sum(besco1)
        out2=np.sum(besco2)
        if out1<0:
            out1=0
        if out2<0:
            out2=0
        res1[i,j]=out1
        res2[i,j]=out2

result=cv2.hconcat([res1,res2])
cv2.imshow('',result)
cv2.waitKey()