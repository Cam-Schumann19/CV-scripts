# _____________________________________________________________________
# Camron Schumann  7-23-2016
#
# First attempt to detect an object given a template image. This did not
# work. It is because while searching the video stream for the template it
# is looking for an exact match and will not find one under any change of lighting.
#  Will come back to issue when I know more about Object Detection and OpenCV
# ______________________________________________________________________


import numpy
import os
import cv2
from matplotlib import pyplot as plt
cap = cv2.VideoCapture(0)

template = cv2.imread('template.jpg',0)
w, h = template.shape[::-1]

ret, frame = cap.read()
vidframe = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

methods = ['cv2.TM_CCOEFF']
while(1):
    for meth in methods:
        method = eval(meth)

        # Apply template Matching
        res = cv2.matchTemplate(vidframe, template, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else:
            top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)

        cv2.rectangle(vidframe, top_left, bottom_right, 255, 2)

        plt.subplot(121), plt.imshow(res, cmap='gray')
        plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(vidframe, cmap='gray')
        plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
        plt.suptitle(meth)

        plt.show()
        cv2.imshow('frame', frame)
        cv2.imshow('asfdsf', vidframe)
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break

cv2.destroyAllWindows()

