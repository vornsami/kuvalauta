from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
from wtforms.validators import Optional, InputRequired, ValidationError
import re


class LoginForm(FlaskForm):

    def validate_login(form, field):
        if field.data:
            if not re.search("^([A-Z]|[a-z]|[0-9]|\-|_|@|%|#|\+)+$", field.data):
                raise ValidationError('Input contains illegal characters.')

    username = StringField("Username", [validate_login, InputRequired(), validators.Length(min=3),validators.Length(max=20)])
    password = PasswordField("Password", [validate_login, InputRequired(), validators.Length(min=3),validators.Length(max=20)])
    
    new_username = StringField("New username", [validate_login, Optional(), validators.Length(min=3),validators.Length(max=20)])
    new_password = PasswordField("New password", [validate_login, Optional(), validators.Length(min=3),validators.Length(max=20)])
    class Meta:
        csrf = False