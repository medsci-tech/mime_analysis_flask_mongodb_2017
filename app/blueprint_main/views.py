import datetime
import json
from flask import url_for
from flask import redirect
from flask import render_template

from . import blueprint_main
from ..models import CommonStatistic


@blueprint_main.route('/')
@blueprint_main.route('/index/')
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


@blueprint_main.route('/regions/', methods=['GET', 'POST'])
def regions():
    group_region_doc = {'$group': {
        '_id': {'province': '$province'},
        'count': {'$sum': '$register_count'}}}
    project_region_doc = {'$project': {
        'role': '$_id.province',
        'count': 1,
        '_id': 0}}
    aggregate_list = list()
    aggregate_list.append(group_region_doc)
    aggregate_list.append(project_region_doc)
    ret = CommonStatistic.objects().aggrate(*aggregate_list)
    return json.dumps(ret)


