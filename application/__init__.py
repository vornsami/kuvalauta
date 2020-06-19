from flask import Flask 
UPLOAD_FOLDER = "static/upload/"

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

app.config["THREAD_LIMIT"] = 20

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "login"
login_manager.login_message = "Please login to use this functionality."

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


try: 
    db.create_all()
except:
    pass