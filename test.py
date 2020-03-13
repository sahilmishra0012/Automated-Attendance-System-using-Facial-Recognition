from cv2 import cv2
img=cv2.imread('bo1.jpg') # Converting matrix to frame

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

faces = face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30, 30),flags = cv2.CASCADE_SCALE_IMAGE)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x-100, y-100), (x+w+100, y+h+100), (255, 255, 0), 2)

scale_percent = 60 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA) 

img=img[y-100:y+h+100,x-100:x+w+100]

cv2.imshow('frame', img)

cv2.waitKey(10000)


cv2.destroyAllWindows()