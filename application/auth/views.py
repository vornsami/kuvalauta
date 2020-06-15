from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm

@app.route("/auth/login", methods = ["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                               error = "No such username or password")


    login_user(user)
    return redirect(url_for("main"))
    
@app.route("/auth/logout")
@login_required
def auth_logout():
    logout_user()
    return redirect(url_for("main"))    
    
    
@app.route("/auth/newuser", methods = ["GET", "POST"])
def newuser():
    if request.method == "GET":
        return render_template("auth/newuser.html", form = LoginForm())

    form = LoginForm(request.form)

    if not form.validate():
        return render_template("auth/newuser.html", form = form,
                               error = "invalid input")

    user = User.query.filter_by(name=form.username.data).first()
    if user:
        return render_template("auth/newuser.html", form = form,
                               error = "Username already in use")
                               
    user = User(form.username.data, form.username.data, form.password.data)
    db.session().add(user)
    db.session().commit()

    login_user(user)
    return redirect(url_for("main"))
