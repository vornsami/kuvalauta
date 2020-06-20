from application import db
from application.models import Base

class User(Base):

    __tablename__ = "account"
  
    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

    acc_type = db.Column(db.String(15), nullable=False)

    threads = db.relationship("Thread", backref='account', lazy=True)
    comments = db.relationship("Comment", backref='account', lazy=True)

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True
        
    def roles(self):
        return self.acc_type

    def is_admin(self):
        if self.acc_type == "ADMIN":
            return True        
        return False