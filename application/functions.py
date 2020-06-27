from application import app, db
import os.path

def dateSort(e):
    return e.date_created
def idSort(e):
    return e.id
    
