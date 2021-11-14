import os
from flask import Flask, request, session, send_from_directory
from werkzeug.utils import secure_filename
import logging
import imgcompression as compress

from flask_cors import CORS, cross_origin
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('API Called')

app = Flask(__name__)
UPLOAD_FOLDER = '../public/user_uploaded/'
DOWNLOAD_FOLDER = '../public/user_uploaded/hasil/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER
SESSION_TYPE = "redis"
PERMANENT_SESSION_LIFETIME = 1800
app.config.update(SECRET_KEY=b'BenciTubes2104819')

@app.route('/compress', methods=['POST'])
def fileCompress():
    target=os.path.join(UPLOAD_FOLDER)
    if not os.path.isdir(target):
        os.mkdir(target)
    file = request.files['file'] 
    ratio = request.form['ratio']
    filename = secure_filename(file.filename)
    logger.info(" [] Uploaded File " + str(filename))
    destination= target + filename
    print(destination)
    if not(os.path.exists(destination)):
        file.save(destination)  
    session['uploadFilePath']=destination
    logger.info(" [] File downloaded, proceeding to compression stage")
    compress.mainCompress(filename, ratio)
    response = app.response_class(status=200)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route("/view/<path:name>")
def view_file(name):
    return send_from_directory(
        app.config['DOWNLOAD_FOLDER'], name, as_attachment=False
    )

@app.route("/download/<path:name>")
def download_file(name):
    return send_from_directory(
        app.config['DOWNLOAD_FOLDER'], name, as_attachment=True
    )

if __name__ == "__main__":
    app.secret_key = b'BenciTubes2104819'
    app.run(debug=True,host="0.0.0.0",use_reloader=False, port=8000)
