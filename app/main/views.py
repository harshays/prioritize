from flask import redirect, render_template, flash, g, session, url_for, request, jsonify
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
    user_todo_all = sorted(current_user.todo.all(), key=lambda x: x.created_at)
    user_todo, user_todo_done = filter(lambda x: x.done == False, user_todo_all), filter(lambda x: x.done == True, user_todo_all) 
    user_hashtags_raw = [x.hashtag for x in user_todo]
    user_hashtags_split = [split_tag for hashtag in user_hashtags_raw for split_tag in hashtag.replace("#"," #").split() if split_tag != ""]
    user_todo_hashtags = Counter(user_hashtags_split)
    tags_size = len(user_todo)
    del user_todo_hashtags[""]
    
    if request.method == "POST" and form.validate_on_submit():
        parsed_todo = parse_todo(form.todo.data)
        newtodo = Todo(parsed_todo[0], parsed_todo[1]).save()
        form.todo.data = ""
        url = url_for('main.profile')
        return redirect(url)
    
    return render_template("profile.html", form = form, td = user_todo, hsh = user_todo_hashtags, sz = tags_size, tdone = user_todo_done)

def parse_todo(todo):
    todo = todo.strip().split()
    words = " ".join(filter(lambda x: not x.startswith("#"), todo))
    tags = "".join(filter(lambda x: x.startswith("#"), todo))
    return words, tags

@main.route('/done/<id>', methods=["POST"])
@login_required 
def done(id):
    iid = int(id);
    current_user.todo.filter_by(id = iid).first().toggleDone();
    db.session.commit()
    return url_for('main.profile')

@main.route('/deleteTodo/<id>', methods=["POST"])
@login_required
def deleteTodo(id):
    iid = int(id)
    db.session.query(Todo).filter_by(id = iid).delete()
    db.session.commit()
    return url_for('main.profile')

@main.route('/edit', methods=["POST"])
@login_required 
def editTodo():
    id = request.json['id']
    task_input = request.json['task']
    task, hashtags = parse_todo(task_input)
    current_user.todo.filter_by(id = id).first().editTodo(task, hashtags).save()
    db.session.commit()
    resp = {'url':url_for('main.profile'), 'task':task, 'hashtags':hashtags}
    return jsonify(resp)
