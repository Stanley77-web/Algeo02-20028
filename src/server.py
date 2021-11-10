from flask import Flask, render_template
from werkzeug.utils import redirect
from imagecompression import imgcompression

app = Flask(__name__, compression_folder ='imagecompression')

@app.route("/")
def homepage():
    return render_template('imgcompression.py')

@app.route("/editor")
def upload():
    return render_template('imgcompression.py')

@app.route("/upload")
def upload():
    return render_template('imgcompression.py')

@app.route("/compress")
def compress():
    return render_template('imgcompression.py')

if __name__ == "__main__":
    app.run()

@app.errorhandler(404)
def page_eror(e):
    return redirect("/")