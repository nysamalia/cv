from flask import Flask, send_from_directory, request, abort, jsonify, render_template, url_for, redirect
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# route home 2
@app.route('/home')
def home2():
    return redirect('/')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/file/<path:hahaha>')
def aksesFile(hahaha):
    return send_from_directory('img', hahaha)


if __name__ == '__main__':
    app.run(
        debug = True,
    )