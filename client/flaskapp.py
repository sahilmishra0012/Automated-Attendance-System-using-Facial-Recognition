from flask import Flask, render_template, request,redirect
from cv2 import cv2
import sys

import os
sys.path.insert(1, '/home/samkiller007/Downloads/Projects/Machine Learning/Automated Attendance System/Face Detection/')
import image_embedding

# sys.path.insert(1, '/home/samkiller007/Downloads/Projects/Machine Learning/Automated Attendance System/Face Detection/')
# import image_embedding

app = Flask(__name__,template_folder='')

app.config["IMAGE_UPLOADS"] = "/home/samkiller007/Downloads/Projects/Machine Learning/Automated Attendance System/Dataset/Images"

app.static_folder = 'static'


@app.route('/')
def index():
    return render_template('mobile.html')

@app.route('/capture', methods=['GET','POST'])
def capture():
    if request.method == 'POST':
        print(request.files['image'])
        image = request.files["image"]
        image.save(os.path.join(app.config["IMAGE_UPLOADS"], 'IM11.jpg')) 
        path='/home/samkiller007/Downloads/Projects/Machine Learning/Automated Attendance System/Dataset/Images'
        embeddings=image_embedding.generate_image_encoding(path)
        
        

    return render_template('mobile.html')





if __name__ == '__main__':
    app.run(host = 'localhost', port = 8080, debug=True)
