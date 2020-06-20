from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from application.auth.models import User
from application.functions import delete_user
from application.threads.models import Thread, Comment

from application import app, db
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
    user = User.query.filter_by(username=form.username.data).first()
    if user:
        return render_template("auth/newuser.html", form = form,
                               error = "Username already in use")
                               
    user = User(form.username.data, form.username.data, form.password.data)
    user.acc_type = "USER"
    db.session().add(user)
    db.session().commit()

    login_user(user)
    return redirect(url_for("main"))
@app.route("/auth/options")
@login_required
def options():
    return render_template("auth/options.html", form = LoginForm())


@app.route("/auth/options/change", methods = ["POST"])
@login_required    
def change_name():
    form = LoginForm(request.form)
    
    new_name = request.form.get("new_name")
    
    u = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not u:
        return render_template("auth/loginform.html", form = form,
                               error = "Incorrect username or password")
    if current_user.id != u.id:
        return render_template("auth/loginform.html", form = form,
                               error = "Incorrect username or password")
    
    user = User.query.filter_by(name=new_name).first()
    if user:
        return render_template("auth/newuser.html", form = form,
                               error = "Username already in use")
    user = User.query.filter_by(username=new_name).first()
    if user:
        return render_template("auth/newuser.html", form = form,
                               error = "Username already in use")
    
    u.name = new_name
    db.session().commit()

    return redirect(url_for("main"))
@app.route("/auth/options/delete", methods = ["POST"])
@login_required    
def delete_self():
    form = LoginForm(request.form)
    
    u = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not u:
        return render_template("auth/loginform.html", form = form,
                               error = "Incorrect username or password")
    if current_user.id != u.id:
        return render_template("auth/loginform.html", form = form,
                               error = "Incorrect username or password")
    
    logout_user
    delete_user(u)
    
    db.session().commit()

    return redirect(url_for("main"))