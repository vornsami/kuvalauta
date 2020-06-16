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
