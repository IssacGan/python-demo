import numpy as np
import cv2
# Load an color image in grayscale
img=cv2.imread('123.jpeg',0)
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
cv2.imwrite('123gray.jpg',img)
k=cv2.waitKey(0)&0xFF
if k==27:
    cv2.destroyAllWindows()
elif k==ord('s'):
    cv2.imwrite('123gray.jpg',img)
    cv2.destroyAllWindows()
    


