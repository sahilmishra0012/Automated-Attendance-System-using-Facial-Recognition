from flask import Flask, render_template, request
from cv2 import cv2

app = Flask(__name__,template_folder='')

app.static_folder = 'static'


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host = 'localhost', port = 8080, debug=True)
