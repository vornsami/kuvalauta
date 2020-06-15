
from application import db
from application.models import Base
from sqlalchemy.sql import text
class Thread(Base):
    
    title = db.Column(db.String(144), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)
    main_comment_id = db.Column(db.Integer, db.ForeignKey('comment.id'),
                           nullable=False)
    
    
    def __init__(self, title):
        self.title = title

    def get_comments(self):
        
        stmt = text("SELECT Comment.* FROM Comment WHERE thread_id = :thread_id;").params(thread_id=self.id)
    
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append(row)
        return list(response)
    def is_main_comment(self, comment):  
        return comment.id == self.main_comment_id
    
    
class Comment(Base):
    
    content = db.Column(db.String(1000), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)
            
    thread_id = db.Column(db.Integer, db.ForeignKey('thread.id'),
                           nullable=False)
    image_id = db.Column(db.Integer, db.ForeignKey('image.id'))
                           
    def __init__(self, content):
        self.content = content  