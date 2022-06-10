#import libraries
import cv2
import numpy

#get images from computer named image
original = cv2.imread(r'image.png')

#make a copy of the image and name it new
new= original.copy()

#show the original image
cv2.imshow('original', original)

#cut the window if key o is presses
while True:
    if cv2.waitKey(1) == ord("o"):
        break
#set values for alpha and beta
alpha = 1.8
beta = 0

# apply the set values to the image
bright = cv2.convertScaleAbs(new, alpha=alpha, beta=beta)

#show the new image
cv2.imshow('brighter',bright)
while True:

#cut the displaying of the new image if key o is presses
    if cv2.waitKey(2) == ord("o"):
        cv2.destroyAllWindows()
        break
