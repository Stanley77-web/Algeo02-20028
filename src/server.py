from flask import Flask, render_template

app = Flask(__name__, compression_folder ='imagecompression')

@app.route("/")
def main():
    return render_template('imgcompression.py')

if __name__ == "__main__":
    app.run()