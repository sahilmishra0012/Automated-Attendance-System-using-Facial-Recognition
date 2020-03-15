from flask import Flask, render_template, request 
from cv2 import cv2

app = Flask(__name__)

app.static_folder = 'static'

@app.route('')
def index():
    return render_template('index.html')

@app.route('/hello', methods=['GET','POST'])
def hello():
        if request.method == 'POST':
            image = request.form['Image']
            get_image = cv2.imread(image,0)
            return cv2.imshow(get_image)
        else:
            return render_template('test.html')


if __name__ == '__main__':
    app.run(host = 'localhost', port = 3000, debug=True)