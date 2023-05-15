#Import libraries
import numpy as np
import cv2
#Load the cascade
face_detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#Read the input image
img = cv2.imread('/Users/joshna/face.jpg')
#Convert the image into greyscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#Detect the faces
results = face_detector.detectMultiScale(gray, 1.3, 5)
#Draw rectangles around the faces
for (x,y,w,h) in results:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
#Display the output
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()