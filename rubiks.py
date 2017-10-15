import numpy as np
import cv2
from cv2 import *

im = cv2.imread('yellowrsz.png')
im = cv2.bilateralFilter(im,9,75,75)
im = cv2.fastNlMeansDenoisingColored(im,None,10,10,7,21)


# il va falloir choisir un "color space" qui convient pour mieux traiter les couleurs

# HSV image
hsv_img = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)   
cv2.imshow("HSV", hsv_img)

# LAB image
lab_img = cv2.cvtColor(im, cv2.COLOR_BGR2LAB)
cv2.imshow("LAB", lab_img)

# YCrCb image
ycrcb_img = cv2.cvtColor(im, cv2.COLOR_BGR2YCrCb)
cv2.imshow("YCrCb", ycrcb_img)


COLOR_MIN = np.array([20, 100, 100],np.uint8)       # HSV color code lower and upper bounds
COLOR_MAX = np.array([30, 255, 255],np.uint8)       # color yellow 

frame_threshed = cv2.inRange(hsv_img, COLOR_MIN, COLOR_MAX)     # Thresholding image
imgray = frame_threshed
ret,thresh = cv2.threshold(frame_threshed,127,255,0)
_, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print(type(contours))
print(contours)
for cnt in contours:
    x,y,w,h = cv2.boundingRect(cnt)
    print(x,y)
    cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)
cv2.imshow("Show",im)
cv2.imwrite("extracted.jpg", im)
cv2.waitKey()
cv2.destroyAllWindows()