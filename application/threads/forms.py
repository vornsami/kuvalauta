from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import StringField, TextAreaField, validators
from wtforms.validators import Optional, InputRequired, ValidationError
import re

class CommentForm(FlaskForm):
    # Kuvatiedoston validointi
    def validate_file(form, field):
        if field.data:
            if not re.search(".*(.)(png|jpg|jpeg|PNG|JPG|JPEG|GIF|gif)$", field.data.filename):
                raise ValidationError('Incorrect file format')

    comment = TextAreaField(("Comment"), [InputRequired(), validators.Length(min=1), validators.Length(max=1000)])
    image = FileField(("Image File"), [validate_file, validators.Optional()])
 
    class Meta:
        csrf = False

class ThreadForm(CommentForm):
    title = StringField(("Thread title"), [validators.Length(max=144)])
    
    class Meta:
        csrf = False
 