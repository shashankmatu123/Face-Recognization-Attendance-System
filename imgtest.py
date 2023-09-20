import cv2
import numpy as np


img1 = cv2.imread('C:/Users/ANAS/Pictures/photos/a25.jpg')
img2 = cv2.imread('C:/Users/ANAS/Pictures/photos/login.png')

img1 = cv2.resize(img1,(1000,500))
img2 = cv2.resize(img2,(300,300))
print(img1)
"""#add = cv2.addWeighted(img1,0.8,img2,0.4,0)
row,cols,channels = img2.shape
roi = img1[0:row , 0:cols]
img2gry = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret,mask = cv2.threshold(img2gry,200,255,cv2.THRESH_BINARY_INV)
mask_inv = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_and(roi,roi,mask=mask_inv)
img2_fg = cv2.bitwise_and(img2,img2,mask=mask)

fram = cv2.add(img1_bg,img2_fg)
img1[0:row , 0:cols] = fram

cv2.imshow('res',img1)"""
cv2.waitKey(0)
cv2.destroyAllWindows()
