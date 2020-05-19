from application import app, db
from flask import render_template, request
from application.threads.models import Thread

@app.route("/threads/new/")
def threads_form():
    return render_template("threads/newthread.html")

@app.route("/threads/", methods=["POST"])
def threads_create():

    t = Thread(request.form.get("title"))

    db.session().add(t)
    db.session().commit()
    return "hello world!"