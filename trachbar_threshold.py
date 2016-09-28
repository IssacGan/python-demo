# -*- coding: utf-8 -*-
"""
Created on Sun Jan 5 13:51:34 2014
@author: duan
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt
def nothing(x):
    pass

img=cv2.imread('/home/issac/Pictures/Webcam/hand.jpg',0)
canny_img=img
cv2.namedWindow('image')

cv2.createTrackbar('maxVal','image',0,255,nothing)
cv2.createTrackbar('minVal','image',0,255,nothing)
switch='0:OFF\n1:ON'
cv2.createTrackbar(switch,'image',0,1,nothing)
while(1):
    cv2.imshow('image',canny_img)
    k=cv2.waitKey(1)&0xFF
    if k==27:
        break
    minval=cv2.getTrackbarPos('minVal','image')
    maxval=cv2.getTrackbarPos('maxVal','image')
    s=cv2.getTrackbarPos(switch,'image')
    if s==0:
        canny_img=img
    else:
        canny_img=cv2.Canny(img,minval,maxval)
cv2.destroyAllWindows()
