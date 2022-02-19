import cv2

#Trained DataSet

trainedDataset=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#read image
img=cv2.imread('images/3.jpg')

#convert to grayscale

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=trainedDataset.detectMultiScale(gray)
print(faces)
for x,y,w,h in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow('Photo',img)
cv2.waitKey()