#!/usr/bin/env python
from flask import Flask, request, session
from flask.ext.script import Manager, Server
from random import SystemRandom
from datetime import timedelta

app = Flask(__name__, static_url_path='')
manager = Manager(app)
manager.add_command("runserver", Server(
    use_debugger = True,
    use_reloader = True,
    host = 'localhost')
)

@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=45)
    session.modified = True

@app.route('/')
def root():
    return app.send_static_file('index.html')

from app.Biblioteca.EventPlanner import EventPlanner
app.register_blueprint(EventPlanner)



#Application code starts here


#Application code ends here

if __name__ == '__main__':
    app.config.update(
      SECRET_KEY = repr(SystemRandom().random())
    )
    manager.run()
