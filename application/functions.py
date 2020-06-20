from application import app, db
from application.threads.models import Thread, Comment
from application.images.models import Image
import os.path

def threadSort(t):
    c = Comment.query.filter_by(thread_id = t.id).all()
    c.sort(key=dateSort,reverse=True)
    return c[0].date_modified
def dateSort(e):
    return e.date_modified
def idSort(e):
    return e.id

def delete_thread_comments(thread):

    c = Comment.query.filter_by(thread_id = thread.id)
    for comment in c:
        delete_comment(comment)
    

def delete_comment(comment):
    i = Image.query.filter_by(id = comment.image_id).first()
    if i is not None:
        os.remove(os.path.join(
            'application', app.config["UPLOAD_FOLDER"], i.filename))
        db.session.delete(i)
    db.session.delete(comment)
    
    
def delete_extra_threads():
    thrs = Thread.query.all()
    if len(thrs) > app.config["THREAD_LIMIT"]:
        thrs.sort(key=threadSort)
        t = thrs[0]
        
        delete_thread_comments(t)

        db.session().delete(t)
        db.session().commit()
        
