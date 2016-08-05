# _____________________________________________________________________
# Camron Schumann  8-01-2016
#
# Performing some basic image processing operations on an image to learn
# capabilities and techniques of computer vision
# ______________________________________________________________________

import cv2
import numpy as np


countR = cv2.imread('countryRoad.jpg',0)
countC = cv2.imread('countryRoad.jpg',-1)
cv2.waitKey(0)


ROi = cv2.equalizeHist(countR)
edges = cv2.Canny(countR,50,250)
r,c = edges.shape
a, b = countR.shape
print a,b
ROI = edges[(r/2):r, 0:c]


cv2.imshow('country road', countR)
cv2.imshow('country road edges', edges)
cv2.imshow('ROI Space', ROI)
cv2.waitKey(0)

laplacian = cv2.Laplacian(ROI,cv2.CV_64F)
sobelx = cv2.Sobel(ROI,cv2.CV_64F,1,0,ksize=5)
#
cv2.imshow('laplacian',edges)
cv2.imshow('sobelx', sobelx)
cv2.waitKey(0)

minLineLength = 100
maxLineGap = 100
lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)
for x1,y1,x2,y2 in lines[0]:
    cv2.line(countC,(x1,y1),(x2,y2),(0,255,0),2)

cv2.imshow(countC)