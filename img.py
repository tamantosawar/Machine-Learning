import cv2
#img=cv2.imread('/home/taman/ml/fl.jpg',1)
img1=cv2.imread('/home/taman/ml/fl1.jpeg',1)
(h,w)=img1.shape[:2]
while True:
	j=int(raw_input('enter how much portion of image u want to see 1/2 or 1/3 or 1/4:'))
	i=img1[0:h/j,0:w/j]
	cv2.imshow('half',i)
	cv2.waitKey(0)

