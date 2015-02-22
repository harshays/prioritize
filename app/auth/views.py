from flask import render_template, session, g, flash, redirect, url_for, request 
from flask.ext.login import login_user, login_required, logout_user

from . import auth 
from forms import LoginForm, RegisterForm 
from .. import db, login_manager
from ..models import User


@auth.route('/login', methods=["GET","POST"])
def login():
    form = LoginForm 
    if request.method == "GET":
        return render_template("base.html")
    
    if form.validate_on_submit():
        user = User.get_username(form.username.data)
        login_user(user, form.remember_me.data)
        return redirect('/')

    return render_template("base.html")

@auth.route("/register", methods = ["GET", "POST"])
def register():
    form = RegisterForm()

    if request.method == "GET":
        return render_template("base.html")
    
    elif request.method == "POST":
        if form.validate_on_submit():
            newuser = User(form.username.data, form.password.data)
            db.session.add(newuser)
            # no need to commit, db commit on teardown is true
            login_user(newuser, False)
            return redirect('/')
        
        return render_template("base.html")
  

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You've been logged out")
    redirect("/")

    
