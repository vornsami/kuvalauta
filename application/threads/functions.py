from application import app, db
import os.path
from application.threads.models import Thread, Comment
from application.images.models import CommentImage    
from application.functions import dateSort

def threadSort(t):
    c = Comment.query.filter_by(thread_id = t.id).all()
    c.sort(key=dateSort,reverse=True)
    return c[0].date_modified
    
def delete_thread_comments(thread):

    c = Comment.query.filter_by(thread_id = thread.id)
    for comment in c:
        delete_comment(comment)
    

def delete_comment(comment):
    i = CommentImage.query.filter_by(id = comment.image_id).first()
    if i:
        delete_image(i)
    db.session.delete(comment)
    
def delete_image(image):
    try:
        os.remove(os.path.join(
            'application', app.config["UPLOAD_FOLDER"], str(image.id) + image.fileformat))
    except:
        print("Image not in filesystem")
    db.session.delete(image)
    
def delete_extra_threads():
    thrs = Thread.query.all()
    if len(thrs) > app.config["THREAD_LIMIT"]:
        thrs.sort(key=threadSort)
        t = thrs[0]
        
        delete_thread_comments(t)

        db.session().delete(t)
        db.session().commit()
        
def delete_user(user):
    t = Thread.query.filter_by(account_id = user.id).all()
    
    for thread in t:
        delete_thread_comments(thread)
        db.session.delete(thread)
    c = Comment.query.filter_by(account_id = user.id).all()
    
    for comment in c:
        delete_comment(comment)
    db.session().delete(user)

