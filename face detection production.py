from cv2 import cv2
import numpy as np
import requests

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while(True):
    img_res = requests.get("http://192.168.43.1:8080/shot.jpg") # Fetching requests from the IP
    img_arr = np.array(bytearray(img_res.content), dtype = np.uint8) # Converting received contents to matrix

    
    img=cv2.imdecode(img_arr,-1) # Converting matrix to frame
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30, 30),flags = cv2.CASCADE_SCALE_IMAGE)
    
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x-50, y-50), (x+w+50, y+h+50), (255, 255, 0), 2)
        
    scale_percent = 60 # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA) 
   
    cv2.imshow('frame', resized)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break


cv2.destroyAllWindows()