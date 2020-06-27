from application import app, db
from flask import render_template, request, redirect, url_for
from flask_login import login_required
from application.threads.models import Thread, Comment
from application.functions import idSort
from application.threads.functions import delete_extra_threads
from application.threads.forms import ThreadForm, CommentForm
from flask_login import current_user
from application.auth.models import User
from application.images.models import CommentImage
from werkzeug.datastructures import CombinedMultiDict
from werkzeug.utils import secure_filename
import os.path

@app.route("/thread/newthread/")
@login_required
def threads_form():
    try:
        return render_template("threads/newthread.html", form = ThreadForm())
    except:
        print("Something went wrong.")
    return redirect(url_for("page_404"))
    
@app.route("/thread/", methods=["POST"])
@login_required
def threads_create():
    try:
        form = ThreadForm(CombinedMultiDict((request.files, request.form)))
        
        if not form.validate():
            return render_template("threads/newthread.html", form = form, 
                               error = "Invalid input. Make sure you have content in your comment and that any attachments are in correct formats.")
        
        image = form.image.data
        image_id = None
        if image is not None:
            image_id = add_image(image)
        
        t = Thread(form.title.data)
        t.account_id = current_user.id
            
        db.session().add(t)
        db.session().commit()
        
        c = Comment(form.comment.data)
        c.account_id = current_user.id
        c.thread_id = t.id
        
        if image_id:
            c.image_id = image_id

        db.session().add(c)
        db.session().commit()
        
        delete_extra_threads()
        
        return redirect(url_for("main"))
    except:
        print("Something went wrong.")
        db.session().rollback()
        
        if t:
            db.session().delete(t)
        if image:
            db.session().delete(image)
        
    return redirect(url_for("page_404"))
    
@app.route("/thread/<thread_id>", methods = ["GET", "POST"])
def threads_page(thread_id):
    try:
        thread = Thread.query.filter_by(id = thread_id).first()
        
        if thread is None:
            return render_template(url_for('main'))
        
        if request.method == "GET" or thread.exceeds_comment_count():
            return render_template("threads/threadpage.html", thread = thread, form = CommentForm())
        
        form = CommentForm(CombinedMultiDict((request.files, request.form)))
        
        if not form.validate():
            return render_template("threads/threadpage.html", thread = thread, form = form,
                                   error = "Invalid input. Make sure you have content in your comment and that any attachments are in correct formats.")
        if not current_user.is_authenticated:
            return render_template("threads/threadpage.html", thread = thread, form = form,
                                   error = "You need to be logged in")
        
        
        
        image = form.image.data
        image_id = None
        if image is not None:
            image_id = add_image(image)
        
        c = Comment(form.comment.data)
        
        c.account_id = int(current_user.id)
        c.thread_id = int(thread_id)
        
        if image_id:
            c.image_id = image_id
        
        db.session().add(c)
        db.session().commit()
        return render_template("threads/threadpage.html", thread = thread, form = CommentForm())
    except:
        print("Something went wrong.")
        db.session().rollback()
    return redirect(url_for("page_404"))


def add_image(image):
    imgs = CommentImage.query.all()
            
        
    # Määritellään tiedostonimi
    
    filename, file_extension = os.path.splitext(image.filename)
    
    i = CommentImage(image.filename)
    i.fileformat = file_extension
    i.image_data = image.read()
            
    db.session().add(i)
    db.session().commit()
    
    return i.id