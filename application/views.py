from flask import Flask, flash, request, redirect, url_for, render_template
from application import app
from application.threads.models import Thread
import os
from werkzeug.utils import secure_filename

import urllib.request
@app.route("/")
def main():
    return render_template("main.html", threads = Thread.query.all())


@app.route('/image/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename='upload/' + filename), code=301)

@app.route("/upload", methods = ["GET", "POST"])
def upload_form():
    if request.method == "GET":
        return render_template('upload.html')

    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return render_template('upload.html', filename=filename)