import os
from flask import Flask, flash, request, redirect, url_for, session, render_template
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin
import logging
import imgcompression as compress
import time

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger('API Called')


UPLOAD_FOLDER = '../src/components/static/user_uploaded'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
SESSION_TYPE = "redis"
PERMANENT_SESSION_LIFETIME = 1800
app.config.update(SECRET_KEY=b'BenciTubes2104819')

@app.route('/upload', methods=['POST', 'GET'])
def fileUpload():
    target=os.path.join(UPLOAD_FOLDER)
    if not os.path.isdir(target):
        os.mkdir(target)
    file = request.files['file'] 
    ratio = request.form['ratio']
    filename = secure_filename(file.filename)
    logger.info(" [] Uploaded File " + str(filename))
    destination="/".join([target, filename])
    if os.path.exists(destination):
        os.remove(destination)
    file.save(destination)
    session['uploadFilePath']=destination
    logger.info(" [] File downloaded, proceeding to compression stage")
    newImage = compress.mainCompress(filename, ratio)
    # time.sleep(60)
    response = app.response_class(status=200)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

#@app.route('/compress', methods=['GET','POST'])
#def imagecompress():
 #   f = open(.../Algeo02-20028/test/react-flask-app/src/components/static/user_uploaded/)

 #   return newimage

if __name__ == "__main__":
    app.secret_key = b'BenciTubes2104819'
    app.run(debug=True,host="0.0.0.0",use_reloader=False, port=8000)

CORS(app, expose_headers='Authorization')