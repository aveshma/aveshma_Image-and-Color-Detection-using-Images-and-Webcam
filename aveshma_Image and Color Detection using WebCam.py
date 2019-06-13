
import numpy as np #import numpy package
import cv2         #mport opencv package


# Initialize camera
cap = cv2.VideoCapture(0) # 0- Primary camera ,1- External camera
                          # Use cv2.imread('./images/nemo0.jpg') to detect the locally stored image

# colour to be masked - blue. Note you can change the pixel value from RGB color space code to mask any desired color of image
lim1 = [100, 100, 100] # Setting the lower pixel for blue (BGR)
lim2 = [150, 150, 255] # Setting the upper pixel for blue (BGR)

# Video Loop
while True:
 ret, frame = cap.read() # Read the image
 if ret == True:
  hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) #BGR to HSV color conversion for the input image
 else:
  continue

# Do the processing
 lower = np.array(lim1)    #define the lower range of blue color
 upper = np.array(lim2)    #define the upper range of blue color
 mask  = cv2.inRange(hsv, lower, upper) # Masking of the image to produce a binary image
 output = cv2.bitwise_and(frame, frame, mask= mask) # The masked blue part of the image/AND is used for part extraction of the image
 
 # Show the image
 cv2.imshow('image',frame)
 cv2.imshow('mask',mask)
 cv2.imshow('output',output)
 
 # End the video loop
 if cv2.waitKey(1) == 27:  #Escape key (ASCII code : 27):
   break

# Close and exit from camera
cap.release() #release the camera device resource
cv2.destroyAllWindows() #to close all the active windows