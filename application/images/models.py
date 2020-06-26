from application import db
from application.models import Base



class CommentImage(Base):

    __tablename__ = "image"
  
    name = db.Column(db.String(144), nullable=False)
    filename = db.Column(db.String(144), nullable=False)
    
    image_data = db.Column(db.LargeBinary(), nullable=False)
    

    def __init__(self, name):
        self.name = name
  
    def get_id(self):
        return self.id



