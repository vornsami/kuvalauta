from application import app, db
from application.threads.models import Thread, Comment

def threadSort(t):
    c = Comment.query.filter_by(thread_id = t.id).all()
    c.sort(key=dateSort,reverse=True)
    return c[0].date_modified
def dateSort(e):
    return e.date_modified
def idSort(e):
    return e.id