import os 
from flask.ext.script import Manager
from app import db, create_app 

app = create_app('production')
manager = Manager(app)

@manager.command
def dbsetup():
    db.drop_all()
    db.create_all()
    db.session.commit()

if __name__ == "__main__":
    manager.run()

