# _____________________________________________________________________
# Camron Schumann  8-01-2016
#
# Import road images and it will try to detect the road and then super impose
# green lines on projected path.
# ______________________________________________________________________

import cv2
import numpy as np


#importing image and converting to grayscale
street = 'countryRoad.jpg'
img = cv2.imread(street,-1)
cv2.imshow('original',img)
gray = cv2.imread(street,0)

#Creating a region of interest (bottom of image where road would be)
r, c = gray.shape
rroi = r/2+20
print rroi
ROI = gray[rroi:r, 0:c]

#Performing cv2's edges function to detect lines in image
edges = cv2.Canny(ROI,50,150,apertureSize = 3)
print edges.dtype

#Performing sobelx function to blur lines for fewer breakpoints
sobelx = cv2.Sobel(edges,cv2.CV_8UC1,1,0,ksize=5)
print sobelx.dtype

#Using a line finder tool in openCV
minLineLength = 10
maxLineGap = 10
lines = cv2.HoughLinesP(sobelx,1,np.pi/180,80,minLineLength,maxLineGap)
test = [[[20, 100, 20, 100]],[[40, 40, 200, 200]]]
for i in lines:
    x1 = i[0][0]
    x2 = i[0][1]
    y1 = i[0][2]
    y2 = i[0][3]
    cv2.line(img,(x1,x2+rroi),(y1,y2+rroi),(0,255,0),2)
# print lines

#Showing images step by step
cv2.imshow('ROI',ROI)
cv2.imshow('sobelx',sobelx)
cv2.imshow('edges',edges)
cv2.imshow('LaneDetection.jpg',img)
cv2.waitKey(0)