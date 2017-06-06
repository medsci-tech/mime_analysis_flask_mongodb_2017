import datetime
import json
from flask import url_for
from flask import redirect
from flask import render_template

from . import blueprint_time
from ..models import Hospital
from ..models import Doctor


@blueprint_time.route('/')
def index():
    hospital = Hospital()
    hospital.name = '光谷同济'
    hospital.level = '三级甲等'
    hospital.province = '湖北'
    hospital.city = '武汉'
    hospital.save()
    return 'save hospital'
