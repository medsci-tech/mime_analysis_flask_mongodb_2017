import json
import datetime
from flask import render_template

from . import blueprint_city
from ..models import Doctor
from ..models import CityStatistic


@blueprint_city.route('/')
@blueprint_city.route('/index/')
def index():
    register_count = Doctor.objects.count()
    authorize_count = Doctor.objects(__raw__={'id_num': {'$exists': True}}).count()
    ret = {'register_count': register_count, 'authorize_count': authorize_count,}
    render_template('city/city.html', ret=ret)

