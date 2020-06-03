
from application import db
from application.models import Base

class Thread(Base):
    
    title = db.Column(db.String(144), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)
    main_comment_id = db.Column(db.Integer, db.ForeignKey('comment.id'),
                           nullable=False)
    def __init__(self, title):
        self.title = title
        
class Comment(Base):
    
    content = db.Column(db.String(1000), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)
                         
    threads = db.relationship("Thread", backref='comment', lazy=True)
                           
    def __init__(self, content):
        self.title = content