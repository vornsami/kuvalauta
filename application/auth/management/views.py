from flask import render_template, request, redirect, url_for
from flask_login import login_required
from application.auth.models import User
from application.threads.functions import delete_thread_comments, delete_comment, delete_image
from application.threads.models import Thread, Comment
from application.images.models import CommentImage

from application import app, db, login_manager, login_required


@app.route("/thread/<thread_id>/delete", methods=["POST"])
@login_required(role="ADMIN")
def admin_delete_thread(thread_id):
    try:
        t = Thread.query.filter_by(id = thread_id).first()
        
        if not t:
            return redirect(url_for('main'))
        
        delete_thread_comments(t)

        db.session.delete(t)
        db.session().commit()

        return redirect(url_for('main'))
    except:
        print("Something went wrong.")
        db.session().rollback()
    return redirect(url_for("page_404"))

    
@app.route("/comment/<comment_id>/delete", methods=["POST"])
@login_required(role="ADMIN")
def admin_delete_comment(comment_id):
    try:
        c = Comment.query.filter_by(id = comment_id).first()
        
        if not c:
            return redirect(url_for('main'))
        
        
        t_id = c.thread_id
        delete_comment(c)
        db.session().commit()

        return redirect(url_for('threads_page', thread_id = t_id)) 
    except:
        print("Something went wrong.")
        db.session().rollback()
    return redirect(url_for("page_404"))        

@app.route("/comment/<comment_id>/delete/image", methods=["POST"])
@login_required(role="ADMIN")
def admin_delete_image(comment_id):
    try:    
        c = Comment.query.filter_by(id = comment_id).first()
        
        if not c:
            return redirect(url_for('main'))
        
        t_id = c.thread_id
        i = CommentImage.query.filter_by(id = c.image_id).first()
        
        if not i:
            return redirect(url_for('threads_page', thread_id = t_id))

        delete_image(i)
        c.image_id = None
        db.session().commit()

        return redirect(url_for('threads_page', thread_id = t_id))
    except:
        print("Something went wrong.")
        db.session().rollback()
    return redirect(url_for("page_404"))
    