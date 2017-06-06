import datetime
import json
from flask import url_for
from flask import redirect
from flask import render_template

from . import blueprint_time
from ..models import CommonStatistic


@blueprint_time.route('/')
@blueprint_time.route('/index/')
def index():
    register_count = CommonStatistic.objects.sum('register_count')
    authorize_count = CommonStatistic.objects.sum('authorize_count')
    order_count = CommonStatistic.objects.sum('order_count')
    payment_count = CommonStatistic.objects.sum('payment_count')

    ret = {
        'register_count': register_count,
        'authorize_count': authorize_count,
        'order_count': order_count,
        'payment_count': payment_count,
    }
    return json.dumps(ret)


@blueprint_time.route('/regions/', methods=['GET', 'POST'])
def regions():
    group_region_doc = {'$group': {
        '_id': {'province': '$province', 'day': '$day'},
        'count': {'$sum': '$register_count'}}}
    project_region_doc = {'$project': {
        'role': '$_id.role',
        'day': '$_id.day',
        'count': 1,
        '_id': 0}}
    return json.dumps(regions_ret)
