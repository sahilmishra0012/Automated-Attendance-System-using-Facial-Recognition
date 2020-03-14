from cv2 import cv2
import numpy as np
import requests
from skimage.transform import resize


def extract_face(image_path,image_size,margin):
    img=cv2.imread(image_path)

    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        
    faces = face_cascade.detectMultiScale(img,scaleFactor=1.1,minNeighbors=5,minSize=(30, 30),flags = cv2.CASCADE_SCALE_IMAGE)
    x=faces[0][0]
    y=faces[0][1]
    w=faces[0][2]
    h=faces[0][3]
    
    cropped = img[y-margin//2:y+h+margin//2,x-margin//2:x+w+margin//2, :]
    img = resize(cropped, (image_size, image_size), mode='reflect')
    return img
