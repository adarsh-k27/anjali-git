#my creation for practise

import cv2 
import numpy as np
#load cascade file for detecting face

cascade_path="haarcascade_frontalface_default_net.xml"
face_detection_cascade = cv2.CascadeClassifier(cascade_path)
# read image from input
path="images/img1.jpg"
img=cv2.imread(path)
print(img)
#convert Image iNto Gray Scale For Detect
gray_scale_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Detect faces from image using Cascade (multiple faces)
faces_detect=face_detection_cascade.detectMultiScale(gray_scale_image,2.1,5)

print(faces_detect)
#iterate over all face we detect and draw line

for (x,y,w,h) in faces_detect:
     sub_face_img = gray_scale_image[y:y+h, x:x+w]
     resized = cv2.resize(sub_face_img, (200, 200))
     normalize = resized/255.0
     print(normalize.shape)
     reshaped = np.reshape(normalize, (200, 200, 1))
     cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)
#display output
cv2.imshow("img", img)
cv2.waitKey()

