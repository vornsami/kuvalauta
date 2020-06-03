from application import app, db
from flask import render_template, request
from flask_login import login_required
from application.threads.models import Thread
from application.threads.forms import ThreadForm

@app.route("/threads/newthread/")
@login_required
def threads_form():
    return render_template("threads/newthread.html", form = ThreadForm())

@app.route("/threads/", methods=["POST"])
@login_required
def threads_create():
    form = TaskForm(request.form)
    
    if not form.validate():
        return render_template("threads/newthread.html", form = form, 
                           error = "Content does not meet requirements")
    
    t = Thread(form.title.data)
    t.account_id = current_user.id
    
    c = Comment(form.comment.data)
    db.session().add(c)
    db.session().commit()
    
    t.main_comment_id = c.id
    
    db.session().add(t)
    db.session().commit()
    return redirect(url_for("main"))