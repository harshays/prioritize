from . import db 
from werkzeug import generate_password_hash, check_password_hash
from flask.ext.login import UserMixin, current_user
from . import login_manager 
from datetime import datetime


@login_manager.user_loader 
def load_user(user_id):
    if user_id == None or user_id == 'None':
        user_id = -1
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100), unique = True)
    password_hash = db.Column(db.String(200))

    todo = db.relationship('Todo', backref = 'user', lazy = 'dynamic')

    def __init__(self, u, p):
        self.username = u
        self.set_password(p)

    def __str__(self):
        return "<Username %s>" %(self.username)

    @property 
    def password(self):
        raise AttributeError("password is not a readable attr")

    def set_password(self,p):
        self.password_hash = generate_password_hash(p)

    def check_password(self, formPassword):
        return check_password_hash(self.password_hash, formPassword)

    # functions for Flask-Login
    def is_authenticated(self):
        return True 

    def is_active(self):
        return True 

    def is_anonymous(self):
        return False 

    def get_id(self):
        return unicode(self.id)

    @classmethod
    def get_username(cls, u):
        return cls.query.filter_by(username = u).first()


class Todo(db.Model):
    __tablename__ = "tsodo"
    id = db.Column(db.Integer, index = True, primary_key = True)
    description = db.Column(db.String(100))
    hashtag = db.Column(db.String(100), default = "")
    # priority = db.Column(db.Integer)
    done = db.Column(db.Boolean, default = False)
    created_at = db.Column(db.DateTime,  default = datetime.utcnow)
    creator = db.Column(db.String(100), db.ForeignKey('user.username'))

    def __init__(self, description, hashtag = "", created_at = datetime.utcnow(), creator = current_user):
        self.description = description 
        self.created_at = created_at
        self.hashtag = self.hashtag + " " + hashtag if self.hashtag != None else hashtag
        self.creator = creator.username if creator != None else ""

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def toggleDone(self):
        self.done = not self.done 
        return self 

    def editTodo(self, task, hashtags):
        self.description = task
        self.hashtag = hashtags
        return self 
    

    






