from flask import redirect, url_for, render_template
from application import app
from application.threads.models import Thread
from application.threads.functions import threadSort

@app.route("/")
def main():
    t = Thread.query.all()
    t.sort(key = threadSort, reverse = True)
    return render_template("main.html", threads = t)


@app.route('/image/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename='upload/' + filename), code=301)
