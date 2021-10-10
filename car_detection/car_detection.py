import os

import cv2
import numpy as np

alg="car_detection/carx.xml" 
haar_cascade=cv2.CascadeClassifier(alg)  
dataset="car_detection/datasets"  #making a folder in which our train data is captured
sub_data="sub_dir" #make a dir inside datasets 
path=os.path.join(dataset,sub_data)
if not os.path.isdir(path):
    os.mkdir(path)
(width,height)=(130,100)
  
cam=cv2.VideoCapture(0)

# use esc button to terminate


count=1
while count>0:
    print(count)
    (_,img)=cam.read()
    
    grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face=haar_cascade.detectMultiScale(grayimg,1.1,1)
    for x,y,w,h in face:

        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        slice_face=grayimg[y:y+h ,x:x+w]
        face_resize=cv2.resize(slice_face,(width,height))
        cv2.imwrite("%s/%s.png" % (path,count),face_resize)
        count+=1
       

        
    cv2.imshow("face_detection",img)


    key=cv2.waitKey(10)
    if key==27:
        break
cam.release()
cv2.destroyAllWindows()
