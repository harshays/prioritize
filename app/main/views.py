from flask import redirect, render_template, flash, g, session, url_for, request
from flask.ext.login import current_user, login_required
from . import main
from .forms import TodoForm
from .. import db 
from ..models import User, Todo
from collections import Counter

@main.app_errorhandler(404)
def page_not_found(e):
    return redirect(url_for('main.index'))

@main.app_errorhandler(500)
def page_not_found(e):
    return redirect(url_for('main.index'))

@main.route('/',methods=["GET","POST"])
def index():
    if current_user.is_authenticated():
        url = url_for('main.profile')
        return redirect(url)
    return render_template("index.html")

@main.route('/profile',methods=["GET","POST"])
@login_required
def profile():
    form = TodoForm()

    user_todo_all = current_user.todo.all()
    user_todo, user_todo_done = filter(lambda x: x.done == False, user_todo_all), filter(lambda x: x.done, user_todo_all) 
    user_todo_hashtags = Counter(list(map(lambda x: x.hashtag, user_todo)))
    del user_todo_hashtags[""]
    
    if request.method == "POST" and form.validate_on_submit():
        parsed_todo = parse_todo(form.todo.data)
        newtodo = Todo(parsed_todo[0], parsed_todo[1]).save()
        form.todo.data = ""
        url = url_for('main.profile')
        return redirect(url)
    
    return render_template("profile.html", form = form, td = user_todo, hsh = user_todo_hashtags, sz = len(user_todo))

def parse_todo(todo):
    todo = todo.strip().split()
    words = " ".join(filter(lambda x: not x.startswith("#"), todo))
    tags = "".join(filter(lambda x: x.startswith("#"), todo))
    return words, tags

@main.route('/done', methods=["POST"])
@login_required 
def done():
    pass


