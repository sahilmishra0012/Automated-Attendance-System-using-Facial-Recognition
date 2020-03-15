from flask import Flask, render_template, request,redirect
from cv2 import cv2
import os


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

    return render_template('mobile.html')





if __name__ == '__main__':
    app.run(host = 'localhost', port = 8080, debug=True)
