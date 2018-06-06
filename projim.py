import cv2
img=cv2.imread('/home/taman/ml/fl.jpg',1)
img1=cv2.imread('/home/taman/ml/fl1.jpeg',1)
h1=img1[0:119,0:121]
img[0:119,0:121]=h1
cv2.imshow('half',img)
cv2.waitKey(0)

'''rhalf=img[384:,512:]
cv2.imshow('rhalf',rhalf)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
