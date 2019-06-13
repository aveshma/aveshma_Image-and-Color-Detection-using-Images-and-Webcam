import numpy as np #import numpy package
import cv2         #mport opencv package
import imageio


#Specifyinh the path of an image to read or access
img = cv2.imread('a2.jpg',1)


#BGR to HSV color conversion for the binary image
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)


lim1 = [100, 100, 100]  #Setting the lower pixel for blue (BGR)
lim2 = [150, 150, 255] #Setting the upper pixel for blue (BGR)



lower = np.array(lim1) #define the lower range of blue color
upper = np.array(lim2) #define the upper range of blue color

# Masking of the image to produce a binary image
mask  = cv2.inRange(hsv, lower, upper)

# The masked blue part of the image/AND is a logical operator used for part extraction of the image
output = cv2.bitwise_and(img, img, mask= mask)


 # Show the image
cv2.imshow('image',img)
cv2.imshow('mask',mask)
cv2.imshow('output',output)


#Close the image and exit all the active windows(ASCII code for "ESC-key" is 27)
cv2.imshow('image',img)
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
 cv2.destroyAllWindows()
