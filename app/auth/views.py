from flask import render_template, session, g, flash, redirect, url_for, request 
from flask.ext.login import login_user, login_required, logout_user

from . import auth 
from forms import LoginForm, RegisterForm 
from .. import db, login_manager
from ..models import User


@auth.route('/login', methods=["GET","POST"])
def login():
    form = LoginForm()
    if request.method == "GET":
        return render_template("login.html", form = form)
    
    if form.validate_on_submit():
        user = User.get_username(form.username.data)
        login_user(user, form.remember_me.data)
        url = url_for('main.index')
        return redirect(url)

    return render_template("login.html", form = form)

@auth.route("/register", methods = ["GET", "POST"])
def register():
    form = RegisterForm()

    if request.method == "GET":
        return render_template("register.html", form = form)
    
    elif request.method == "POST":
        if form.validate_on_submit():
            newuser = User(form.username.data, form.password.data)
            db.session.add(newuser)
            db.session.commit()
            # no need to commit, db commit on teardown is true
            login_user(newuser, False)
            url = url_for('main.profile')
            return redirect(url)
        
        return render_template("register.html", form = form)
  

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You've been logged out")
    return redirect("/")

    
