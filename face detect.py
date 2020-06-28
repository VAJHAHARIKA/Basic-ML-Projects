# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 21:27:06 2020

@author: User
"""

import cv2

imagep= "family.jpg"
cascade_path="haarcascade_frontalface_alt.xml"
hfc=cv2.CascadeClassifier(cascade_path)
photo=cv2.imread(imagep)
faces=hfc.detectMultiScale(photo,scaleFactor=1.5,minNeighbors=5,minSize=(30,30))

print("found {0} faces".format(len(faces)))

for (r,l,w,h) in faces:
    cv2.rectangle(photo,(r,l),(r+w,l+h),color=(0,200,0),thickness=2)
    
cv2.imshow("faces found",photo)
cv2.waitKey(0)

