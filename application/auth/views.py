from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from application.auth.models import User
from application.threads.functions import delete_user
from application.threads.models import Thread, Comment

from application import app, db
from application.auth.forms import LoginForm

@app.route("/auth/login", methods = ["GET", "POST"])
def login():
    try:
        if request.method == "GET":
            return render_template("auth/loginform.html", form = LoginForm())

        form = LoginForm(request.form)
        if not form.validate():
            return render_template("auth/loginform.html", form = form,
                                   error = "Invalid input. The username and password must have 3-20 characters, and mustn't contain illegal characters.")
        
        user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
        if not user:
            return render_template("auth/loginform.html", form = form,
                                   error = "No such username or password")

        login_user(user)
        return redirect(url_for("main"))
    except:
        print("Something went wrong.")
        db.session().rollback()
    return redirect(url_for("page_404"))
    
@app.route("/auth/logout")
@login_required
def auth_logout():
    try:
        logout_user()
        return redirect(url_for("main"))   
    except:
        print("Something went wrong.")
        db.session().rollback()
    return redirect(url_for("page_404"))        
    
    
@app.route("/auth/newuser", methods = ["GET", "POST"])
def newuser():
    try:
        if request.method == "GET":
            return render_template("auth/newuser.html", form = LoginForm())

        form = LoginForm(request.form)

        if not form.validate():
            return render_template("auth/newuser.html", form = form,
                                   error = "Invalid input. The username and password must have 3-20 characters, and mustn't contain illegal characters.")

        user = db.session.query(User).filter((User.name == form.username.data) | (User.username == form.username.data)).first()
        if user:
            return render_template("auth/newuser.html", form = form,
                                   error = "Username already in use")
                                   
        user = User(form.username.data, form.username.data, form.password.data)
        user.acc_type = "USER"
        db.session().add(user)
        db.session().commit()

        login_user(user)
        return redirect(url_for("main"))
    except:
        print("Something went wrong.")
        db.session().rollback()
    return redirect(url_for("page_404"))
        
@app.route("/auth/options")
@login_required
def options():
    try:
        return render_template("auth/options.html", form = LoginForm())
    except:
        print("Something went wrong.")
    return redirect(url_for("page_404"))

@app.route("/auth/options/change_name", methods = ["POST"])
@login_required    
def change_name():
    try:
        form = LoginForm(request.form)
        
        if not form.validate():
            return render_template("auth/options.html", form = form,
                                   error = "Invalid input. The username and password must have 3-20 characters, and mustn't contain illegal characters.")
                                   
        new_name = form.new_username.data
        
        if not new_name:
            return render_template("auth/options.html", form = form,
                                   error = "You need to input a new name")
        
        u = User.query.filter_by(username=form.username.data, password=form.password.data).first()
        if not u:
            return render_template("auth/options.html", form = form,
                                   error = "Incorrect username or password")
        if current_user.id != u.id:
            return render_template("auth/options.html", form = form,
                                   error = "Incorrect username or password")
        
        # Tarkastetaan ettei nimi ole jo käytössä, mutta oma käyttäjänimi on edelleen sallittu
        user = db.session.query(User).filter(((User.name == new_name) | (User.username == new_name)) & (User.id != current_user.id)).first()
        if user:
            return render_template("auth/options.html", form = form,
                                   error = "Username already in use")
        
        u.name = new_name
        db.session().commit()

        return redirect(url_for("main"))
    except:
        print("Something went wrong.")
        db.session().rollback()
    return redirect(url_for("page_404"))
    
@app.route("/auth/options/change_username", methods = ["POST"])
@login_required    
def change_username():
    try:
        form = LoginForm(request.form)
        
        if not form.validate():
            return render_template("auth/options.html", form = form,
                                   error = "Invalid input. The username and password must have 3-20 characters, and mustn't contain illegal characters.")
                                   
        new_username = form.new_username.data
        
        if not new_username:
            return render_template("auth/options.html", form = form,
                                   error = "You need to input a new name")
        
        u = User.query.filter_by(username=form.username.data, password=form.password.data).first()
        if not u:
            return render_template("auth/options.html", form = form,
                                   error = "Incorrect username or password")
        if current_user.id != u.id:
            return render_template("auth/options.html", form = form,
                                   error = "Incorrect username or password")
        
        # Tarkastetaan ettei nimi ole jo käytössä, mutta oma käyttäjänimi on edelleen sallittu
        user = db.session.query(User).filter(((User.name == new_username) | (User.username == new_username)) & (User.id != current_user.id)).first()
        if user:
            return render_template("auth/options.html", form = form,
                                   error = "Username already in use")
        
        # Mikäli käyttäjällä on sama käyttäjänimi ja käyttäjätunnus, muutetaan käyttäjänimi myös.
        if u.name == u.username:
            u.name = new_username
            
        u.username = new_username
        
        db.session().commit()

        return redirect(url_for("main"))
    except:
        print("Something went wrong.")
        db.session().rollback()
    return redirect(url_for("page_404"))
    

@app.route("/auth/options/change_password", methods = ["POST"])
@login_required    
def change_password():
    try:
        form = LoginForm(request.form)
        
        if not form.validate():
            return render_template("auth/options.html", form = form,
                                   error = "Invalid input. The username and password must have 3-20 characters, and mustn't contain illegal characters.")
                                   
        new_password = form.new_password.data
        
        if not new_password:
            return render_template("auth/options.html", form = form,
                                   error = "You need to input a new password")
                                   
                                   
        u = User.query.filter_by(username=form.username.data, password=form.password.data).first()
        if not u:
            return render_template("auth/options.html", form = form,
                                   error = "Incorrect username or password")
        if current_user.id != u.id:
            return render_template("auth/options.html", form = form,
                                   error = "Incorrect username or password")
        
        current_user.password = new_password
        db.session().commit()

        return redirect(url_for("main"))    
    except:
        print("Something went wrong.")
        db.session().rollback()
    return redirect(url_for("page_404"))
    
@app.route("/auth/options/delete", methods = ["POST"])
@login_required    
def delete_self():
    try:
        form = LoginForm(request.form)
        
        if not form.validate():
            return render_template("auth/options.html", form = form,
                                   error = "Invalid input. The username and password must have 3-20 characters, and mustn't contain illegal characters.")
                                   
        u = User.query.filter_by(username=form.username.data, password=form.password.data).first()
        if not u:
            return render_template("auth/options.html", form = form,
                                   error = "Incorrect username or password")
        if current_user.id != u.id:
            return render_template("auth/options.html", form = form,
                                   error = "Incorrect username or password")
        
        logout_user
        delete_user(u)
        
        db.session().commit()

        return redirect(url_for("main"))
    except:
        print("Something went wrong.")
        db.session().rollback()
    return redirect(url_for("page_404"))