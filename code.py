import warnings
warnings.filterwarnings("ignore")
import numpy as np
import os
import matplotlib.pyplot as plt
from cv2 import cv2
from sklearn.decomposition import PCA
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import proj3d
from imageio import imread
from skimage.transform import resize
from scipy.spatial import distance
from keras.models import load_model
import keras.backend as K
K.clear_session()

image_dir_basepath = '../data/images/'
names = ['Barack Obama', 'Hillary Clinton']

model_path = '/home/samkiller007/Downloads/Projects/Machine Learning/Automated Attendance System/model/keras/model/facenet_keras.h5'
model = load_model(model_path)

img=cv2.imread('one.jpg')

dim=(160,160)

img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
img=img.resize(160,160,3,1)
print(model.predict_on_batch(img))