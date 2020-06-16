from application import app, db
from flask import render_template, request, redirect, url_for
from flask_login import login_required
from application.threads.models import Thread, Comment
from application.threads.forms import ThreadForm, CommentForm
from flask_login import current_user
from application.images.models import Image
from werkzeug.datastructures import CombinedMultiDict
from werkzeug.utils import secure_filename
import os.path

@app.route("/thread/newthread/")
@login_required
def threads_form():
    return render_template("threads/newthread.html", form = ThreadForm())
    
@app.route("/thread/", methods=["POST"])
@login_required
def threads_create():
    form = ThreadForm(request.form)
    
    if not form.validate():
        return render_template("threads/newthread.html", form = form, 
                           error = "Content does not meet requirements")
    
    t = Thread(form.title.data)
    t.account_id = current_user.id
    
    t.main_comment_id = len(Comment.query.all()) + 1
    
    db.session().add(t)
    db.session().commit()
    
    c = Comment(form.comment.data)
    c.account_id = current_user.id
    c.thread_id = t.id
    
    db.session().add(c)
    db.session().commit()
    
    return redirect(url_for("main"))
    
@app.route("/thread/<thread_id>", methods = ["GET", "POST"])
def threads_page(thread_id):
    thread = Thread.query.filter_by(id = thread_id).first()
    if request.method == "GET":
        return render_template("threads/threadpage.html", thread = thread, form = CommentForm())
    
    form = CommentForm(CombinedMultiDict((request.files, request.form)))
    
    if not form.validate():
        return render_template("threads/threadpage.html", thread = thread, form = form,
                               error = "invalid input")
    if not current_user.is_authenticated:
        return render_template("threads/threadpage.html", thread = thread, form = form,
                               error = "You need to be logged in")
    
    
    
    image = form.image.data
    print(image)
    if image is not None:
        num = len(Image.query.all()) + 1
        filename, file_extension = os.path.splitext(image.filename)
        filename = secure_filename(str(num) + file_extension)
        image.save(os.path.join(
            'application', app.config['UPLOAD_FOLDER'], filename
        ))
    
        i = Image(image.name)
        i.filename = filename
            
        print(filename)
        db.session().add(i)
        db.session().commit()
    
    c = Comment(form.comment.data)
    
    c.account_id = int(current_user.id)
    c.thread_id = int(thread_id)
    
    if image is not None:
        c.image_id = int(i.id)
    
    db.session().add(c)
    db.session().commit()
    return render_template("threads/threadpage.html", thread = thread, form = CommentForm())

