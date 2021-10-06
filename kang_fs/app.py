from flask import Flask,request,jsonify,Response,render_template
from sqlalchemy import create_engine,text
import cv2
import pickle
import pandas as pd
import numpy as np

from sqlalchemy.sql.expression import column

app = Flask(__name__)
camera = cv2.VideoCapture(0)  # use 0 for web camera



def gen_frames():  # generate frame by frame from camera
    while True:
        # Capture frame-by-frame
        success, frame = camera.read()  # read the camera frame
        if (not success):

            break

        else:

            ret, buffer = cv2.imencode('.jpg', frame)

            frame = buffer.tobytes()

            yield (b'--frame\r\n'

                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

                   # concat frame one by one and show result


@app.route('/video_feed')

def video_feed():
 
    """Video streaming route. Put this in the src attribute of an img tag."""

    return Response(gen_frames(),

                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/video',methods=['GET','POST'])

def index():

    """Video streaming home page."""

    return render_template('index.html')


if __name__ == '__main__':
    app.run(host="172.30.16.1", port=8081)

