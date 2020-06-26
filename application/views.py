from flask import redirect, url_for, render_template
from application import app, db
from application.threads.models import Thread, Comment
from application.threads.functions import threadSort
from application.images.models import CommentImage
from application.threads.functions import delete_image
import io
import os.path
from PIL import Image

@app.route("/")
def main():
    try:
        t = Thread.query.all()
        t.sort(key = threadSort, reverse = True)
        return render_template("main.html", threads = t)
    except:
        print("Something went wrong.")
		
        for thread in t:
            print(thread.title)
            comment = Comment.query.filter_by(thread_id = thread.id).first()
            
            if not comment:
                print("!!!!!!")
                db.session.delete(thread)
                db.session.commit()
		
        return redirect(url_for("page_404"))

@app.route("/404page")
def page_404():
    return render_template("404page.html")

@app.route('/image/<image_id>')
def display_image(image_id):

    image = CommentImage.query.filter_by(id = image_id).first()
    if image:
        try:
            image_data = image.image_data
        
            stream = io.BytesIO(image_data)
        
            img = Image.open(stream)
            
            img.save(os.path.join(
                'application', app.config["UPLOAD_FOLDER"], image.filename
            ))    
            return redirect(url_for('static', filename='upload/' + image.filename), code=301)
        except:
            print("Faulty image data, deleting image...")
            delete_image(image)
    
    return redirect(url_for("page_404"))
