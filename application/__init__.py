from flask import Flask 

UPLOAD_FOLDER = "static/upload/"
THREAD_LIMIT = 20
DEFAULT_ADMIN_USERNAME = "admin"
DEFAULT_ADMIN_PASSWORD = "admin"

app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///board.db"
app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

from application import views

from application.threads import models, views
from application.auth import models, views
from application.images import models

from application.auth.models import User
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

app.config["THREAD_LIMIT"] = THREAD_LIMIT           
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "login"
login_manager.login_message = "Please login to use this functionality."

from functools import wraps
from flask_login import current_user

def login_required(role="ANY"):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if not current_user:
                return login_manager.unauthorized()
          
            if not current_user.is_authenticated:
                return login_manager.unauthorized()
            
            unauthorized = False

            if role != "ANY":
                unauthorized = True
                
                
                if current_user.roles() == role:
                    unauthorized = False
                

            if unauthorized:
                return login_manager.unauthorized()
            
            return fn(*args, **kwargs)
        return decorated_view
    return wrapper
    
from application.auth.management import views
    
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


try: 
    db.create_all()
except:
    pass

#Luodaan admin-käyttäjä, mikäli sellaista ei vielä ole    
from application.threads.functions import delete_user

admin = User.query.filter_by(id=1,username=DEFAULT_ADMIN_USERNAME).first()
if not admin:
    user = User.query.filter_by(id=1).first()
    if user:
        delete_user(user)
    u = User(DEFAULT_ADMIN_USERNAME,DEFAULT_ADMIN_USERNAME,DEFAULT_ADMIN_PASSWORD)
    u.acc_type = "ADMIN"
    u.id = 1
    db.session().add(u)
    db.session().commit()