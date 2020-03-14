from cv2 import cv2
import numpy as np
import requests
from skimage.transform import resize


def extract_face(image_path,image_size,margin):
    img=cv2.imread(image_path)
    

    face_cascade = cv2.CascadeClassifier('/home/samkiller007/Downloads/Projects/Machine Learning/Automated Attendance System/Face Detection/haarcascade_frontalface_default.xml')
        
    faces = face_cascade.detectMultiScale(img, 1.3, 5)
    x=faces[0][0]
    y=faces[0][1]
    w=faces[0][2]
    h=faces[0][3]
    
    cropped = img[y-margin//2:y+h+margin//2,x-margin//2:x+w+margin//2, :]
    img = resize(cropped, (image_size, image_size), mode='reflect')
    return img
