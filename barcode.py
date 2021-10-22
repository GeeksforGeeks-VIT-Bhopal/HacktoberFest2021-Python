import cv2 as cv
import numpy as np
from pyzbar.pyzbar import decode 

cap = cv.VideoCapture(0)

while True:
    _,frame = cap.read()

    for barcode in decode(frame):
        print(barcode.data.decode('utf-8'))
        Data = barcode.data.decode('utf-8')
        pts = np.array([barcode.polygon],np.int32)
        pts = pts.reshape((1,-1,2))
        cv.polylines(frame,[pts],True,(0,255,0),3)
        pts2 = barcode.rect
        cv.putText(frame,Data,(pts2[0],pts2[1]),cv.FONT_HERSHEY_COMPLEX_SMALL,0.9,(255,0,255),2)
    cv.imshow("Frame",frame)
    if cv.waitKey(1) & 0xFF == 27:  # Press Escape Key to close all windows
        break
cap.release()
cv.destroyAllWindows()
