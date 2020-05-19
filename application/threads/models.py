
from application import db


class Thread(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    
    title = db.Column(db.String(144), nullable=False)
    
    def __init__(self, title):
        self.title = title