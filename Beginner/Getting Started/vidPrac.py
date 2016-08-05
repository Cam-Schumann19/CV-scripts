# _____________________________________________________________________
# Camron Schumann  7-23-2016
#
# Simple Code to familiarize my self with opening a window and using my
# laptop camera with openCV
# ______________________________________________________________________

import cv2

cap = cv2.VideoCapture(0)

while(1):
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
