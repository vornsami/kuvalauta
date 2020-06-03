from flask import render_template 
from application import app
from application.threads.models import Thread

@app.route("/")
def main():
    return render_template("main.html", threads = Thread.query.all())
    