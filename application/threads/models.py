
from application import app, db
from application.models import Base
from sqlalchemy.sql import text
from application.images.models import CommentImage
from application.auth.models import User
from application.functions import dateSort

class Thread(Base):
    
    title = db.Column(db.String(144), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)
    
    def __init__(self, title):
        self.title = title

    def get_comments(self):
            
        stmt = text("SELECT Comment.* FROM Comment WHERE thread_id = :thread_id;").params(thread_id=self.id)
    
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append(row)
        	
        response = list(response)
        response.sort(key=dateSort)
        return response

    def get_main_comment(self):
        comments = Comment.query.filter_by(thread_id = self.id).order_by(Comment.date_created)
        return comments[0]

    def get_comment_user(self,comment):
        return User.query.filter_by(id = comment.account_id).first()
        
    def exceeds_comment_count(self):
        return Comment.query.filter_by(thread_id = self.id).count() > app.config["COMMENT_LIMIT"]

class Comment(Base):
    
    content = db.Column(db.String(5020), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)
            
    thread_id = db.Column(db.Integer, db.ForeignKey('thread.id'),
                           nullable=False)
    image_id = db.Column(db.Integer, db.ForeignKey('image.id'))
                           
    def __init__(self, content):
        self.content = content  

