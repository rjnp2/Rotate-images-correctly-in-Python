#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 23 15:05:21 2020

@author: rjn
"""
## Rotate images (correctly) with OpenCV in Python

# import the necessary packages
import numpy as np
import imutils
import cv2

img = cv2.imread('/home/rjn/Downloads/24.jpg')
cv2.imshow("original", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# using imutils
# first -> loop over the rotation angles
# second -> loop over the rotation angles again, this time ensuring
# no part of the image is cut off
for angle in np.arange(0, 360, 15):
    
    rotated_Correct = imutils.rotate_bound(img, angle)
    rotated = imutils.rotate(img, angle)
    cv2.imshow("Rotated (Correct)", rotated_Correct)
    cv2.imshow("Rotated (Problematic)", rotated)
    cv2.waitKey(1000)
cv2.destroyAllWindows()
   
# using opencv
# first -> loop over the rotation angles
# second -> loop over the rotation angles again, this time ensuring
# no part of the image is cut off
for angle in np.arange(0, 360, 15):
    # grab the dimensions of the image and then determine the
    # center
    (h, w) = img.shape[:2]
    (cX, cY) = (w // 2, h // 2)
    
    # grab the rotation matrix (applying the negative of the
    # angle to rotate clockwise), then grab the sine and cosine
    # (i.e., the rotation components of the matrix)
    M = cv2.getRotationMatrix2D((cX, cY), angle, 1.0)
    nM = M.copy()
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])
    
    # compute the new bounding dimensions of the image
    nW = int((h * sin) + (w * cos))
    nH = int((h * cos) + (w * sin))
    
    # adjust the rotation matrix to take into account translation
    nM[0, 2] += (nW / 2) - cX
    nM[1, 2] += (nH / 2) - cY
    
    rotated_Correct =cv2.warpAffine(img, nM, (nW, nH))
    rotated = cv2.warpAffine(img, M, (w, h))
    
    cv2.imshow("Rotated (Correct)", rotated_Correct)
    cv2.imshow("Rotated (Problematic)", rotated)
    cv2.waitKey(1000)
cv2.destroyAllWindows()
