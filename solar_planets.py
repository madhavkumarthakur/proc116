import cv2
import time
import os


img=cv2.imread("solar-system.jpg")
cv2.putText(img,
            "sun",(100,80),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,255,255))
cv2.putText(img,
            "Earth",(280,300),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,255,255))
cv2.putText(img,
            "Mercury",(120,160),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,255,255))
cv2.putText(img,
            "venus",(190,300),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,255,255))
cv2.putText(img,
            "Mars",(380,300),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,255,255))
cv2.putText(img,
            "jupiter",(430,80),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,2,(0,255,255))
cv2.putText(img,
            "Saturn",(700,100),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,255,255))
cv2.putText(img,
            "Uranus",(900,100),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,255,255))
cv2.putText(img,
            "Neptune",(1100,100),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,255,255))

cv2.imshow("displayimage",img)
cv2.waitKey(0)