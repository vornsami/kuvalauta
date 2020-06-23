from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
from wtforms.validators import Optional, InputRequired
class LoginForm(FlaskForm):
    username = StringField("Username", [InputRequired(), validators.Length(min=2),validators.Length(max=140)])
    password = PasswordField("Password", [InputRequired(), validators.Length(min=2),validators.Length(max=140)])
    
    new_username = StringField("New username", [Optional(), validators.Length(min=2),validators.Length(max=140)])
    new_password = PasswordField("New password", [Optional(), validators.Length(min=2),validators.Length(max=140)])
    class Meta:
        csrf = False