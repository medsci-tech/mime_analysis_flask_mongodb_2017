from flask import g
from flask import url_for
from flask import session
from flask import redirect
from flask_script import Manager

from app import create_app
from app.models import User

app = create_app('development')
manager = Manager(app=app)


@manager.command
def hello():
    print('Hello Flask!')


@app.before_request
def check_user():
    if 'user_phone' in session:
        g.current_user = User.objects(phone=session['user_phone']).first()
    else:
        g.current_user = None


@app.route('/')
@app.route('/index/')
def index():
    return redirect(url_for('blueprint_time.index'))


if __name__ == "__main__":
    manager.run()
