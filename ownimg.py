#!/usr/bin/python3
import cv2 
import numpy as np 

img = np.zeros((512,512,3))
#cv2.line(img,(0,0),(100,110),(255,0,0),3)
cv2.rectangle(img,(10,65),(330,420),(12,12,2),-1)
cv2.circle(img,(165,250),150,(255,0,0),-1)
cv2.circle(img,(165,250),130,(0,254,0),-1)
cv2.circle(img,(165,250),110,(25,254,0),-1)
cv2.circle(img,(165,250),80,(0,0,253),-1)

print(img)
print(img.shape)
cv2.imshow('owmimg',img)
cv2.waitKey(0)
#cv2.imwrite('own.jpg',img)
cv2.destroyAllWindows()
cv2.imwrite('own.jpg',img)

