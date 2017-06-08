import json
from flask import render_template

from . import blueprint_open_class
from ..models import Doctor


@blueprint_open_class.route('/')
@blueprint_open_class.route('/index/')
def index():
    return render_template('open_class/main.html')

