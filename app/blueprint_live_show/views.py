import json
from flask import render_template

from . import blueprint_live_show
from ..models import Doctor


@blueprint_live_show.route('/')
@blueprint_live_show.route('/index/')
def index():
    return render_template('live_show/index.html')

