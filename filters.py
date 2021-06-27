import cv2
import numpy as np
org=cv2.imread('fateme.jpg',cv2.IMREAD_GRAYSCALE)

def filter(img,size,value):
    # img=cv2.resize(img,(size*100,size*100))
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
    cv2.imshow('', res)
    cv2.waitKey()

#filter(org,3,1/9)
#filter(org,5,1/25)
#filter(org,7,1/49)
filter(org,15,1/255)