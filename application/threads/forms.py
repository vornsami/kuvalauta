from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import StringField, TextAreaField, validators
from wtforms.validators import Optional

class ThreadForm(FlaskForm):
    title = StringField(("Thread title"), [validators.Length(max=144)])
    comment = TextAreaField(("Comment"), [validators.Length(min=2)])
 
    class Meta:
        csrf = False
        
class CommentForm(FlaskForm):
    comment = TextAreaField(("Comment"), [validators.Length(min=2)])
    image = FileField(("Image File"))#, [validators.regexp('/(\w+)(.)(png|jpg|jpeg|PNG|JPG|JPEG)/g'), validators.Optional()])
 
    class Meta:
        csrf = False
