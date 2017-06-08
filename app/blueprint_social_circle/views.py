import json
from flask import render_template

from . import blueprint_social_circle


@blueprint_social_circle.route('/')
@blueprint_social_circle.route('/index/')
def index():
    return render_template('social_circle/index.html')

