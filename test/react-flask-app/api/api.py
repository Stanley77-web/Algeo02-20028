import os
from flask import Flask, flash, request, redirect, url_for, session, render_template
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin
import logging
import imgcompression as compress

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger('API Called')


UPLOAD_FOLDER = '../src/components/static/user_uploaded'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
SESSION_TYPE = "redis"
PERMANENT_SESSION_LIFETIME = 1800
app.config.update(SECRET_KEY=b'BenciTubes2104819')

white = ['http://localhost:8080','http://localhost:9000', 'http://localhost:3000']
@app.after_request
def add_cors_headers(response):
    r = request.referrer[:-1]
    if r in white:
        response.headers.add('Access-Control-Allow-Origin', r)
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Headers', 'Cache-Control')
        response.headers.add('Access-Control-Allow-Headers', 'X-Requested-With')
        response.headers.add('Access-Control-Allow-Headers', 'Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, DELETE')
    return response

@app.route('/upload', methods=['POST'])
def fileUpload():
    target=os.path.join(UPLOAD_FOLDER)
    if not os.path.isdir(target):
        os.mkdir(target)
    file = request.files['file'] 
    ratio = request.form['ratio']
    filename = secure_filename(file.filename)
    logger.info(" [] Uploaded File " + str(filename))
    destination="/".join([target, filename])
    file.save(destination)
    session['uploadFilePath']=destination
    logger.info(" [] File downloaded, proceeding to compression stage")
    compress.mainCompress(filename, ratio)
    response="File Uploaded"
    return response

if __name__ == "__main__":
    app.secret_key = b'BenciTubes2104819'
    app.run(debug=True,host="0.0.0.0",use_reloader=False, port=8000)

CORS(app, expose_headers='Authorization')