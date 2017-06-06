import datetime
import json
from flask import session
from flask import url_for
from flask import redirect
from flask import render_template

from . import blueprint_auth
from .forms import RegisterForm
from .forms import LoginForm
from .utils_sms import generate_code
from .utils_sms import send_sms_code
from ..models import User


@blueprint_auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        session['user_phone'] = form.phone.data
        return redirect(url_for('blueprint_time.index'))

    return render_template('auth/login.html', form=form)


@blueprint_auth.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('user_phone', None)
    return redirect(url_for('blueprint_auth.login'))


@blueprint_auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User.objects(phone=form.phone.data).first()
        user.set_password(form.password.data)
        user.save()
        return redirect(url_for('blueprint_auth.login'))

    return render_template('auth/register.html', form=form)


@blueprint_auth.route('/sms_code/<string:phone>', methods=['GET', 'POST'])
def sms_code(phone):
    user = User.objects(phone=phone).first()
    if not user:
        ret = {'error': 'user not existed'}
        return json.dumps(ret)

    code = generate_code()
    ret = send_sms_code(phone, code)
    if not ret:
        ret = {'error': 'sms code failed'}
        return json.dumps(ret)

    user.sms_code = code
    user.updated_at = datetime.datetime.now()
    user.save()
    ret = {'error': ''}
    return json.dumps(ret)
