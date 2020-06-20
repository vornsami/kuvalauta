from flask import render_template, request, redirect, url_for
from flask_login import login_required
from application.auth.models import User
from application.functions import delete_thread_comments, delete_comment
from application.threads.models import Thread, Comment

from application import app, db, login_manager, login_required


@app.route("/thread/<thread_id>/delete", methods=["POST"])
@login_required(role="ADMIN")
def admin_delete_thread(thread_id):

    t = Thread.query.filter_by(id = thread_id).first()
    delete_thread_comments(t)

    db.session.delete(t)
    db.session().commit()

    return redirect(url_for('main'))
    
@app.route("/comment/<comment_id>/delete", methods=["POST"])
@login_required(role="ADMIN")
def admin_delete_comment(comment_id):
    
    c = Comment.query.filter_by(id = comment_id).first()
    t_id = c.thread_id
    delete_comment(c)
    db.session().commit()

    return redirect(url_for('threads_page', thread_id = t_id))    
    
    