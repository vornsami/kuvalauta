
from application import db
from application.models import Base
from sqlalchemy.sql import text
from application.images.models import Image
from application.auth.models import User
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
    def get_main_comment(self):
        
        return Comment.query.filter_by(id = self.main_comment_id).first()

    def get_image_filename(self,comment):
        image = Image.query.filter_by(id = comment.image_id).first()
        
        if image is not None:
            return image.filename
        return None

    def get_comment_user(self,comment):
        return User.query.filter_by(id = comment.account_id).first()

class Comment(Base):
    
    content = db.Column(db.String(1000), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)
            
    thread_id = db.Column(db.Integer, db.ForeignKey('thread.id'),
                           nullable=False)
    image_id = db.Column(db.Integer, db.ForeignKey('image.id'))
                           
    def __init__(self, content):
        self.content = content  

