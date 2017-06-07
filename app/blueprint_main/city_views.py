import json
import datetime

from . import blueprint_main
from ..models import CityStatistic


@blueprint_main.route('/months/<int:year>', methods=['GET', 'POST'])
def months(year=datetime.datetime.now().year):
    match_doc = {'$match': {'year': year}}
    group_doc = {'$group': {
        '_id': {'month': '$month'},
        'register_count': {'$sum': '$register_count'},
        'authorize_count': {'$sum': '$authorize_count'},}}
    project_doc = {'$project': {
        'month': '$_id.month',
        'register_count': 1,
        'authorize_count': 1,
        '_id': 0}}

    aggregate_list = list()
    aggregate_list.append(match_doc)
    aggregate_list.append(group_doc)
    aggregate_list.append(project_doc)
    ret = CityStatistic.objects().aggregate(*aggregate_list)

    return json.dumps(ret)


@blueprint_main.route('/days/<int:year>/<int:month>', methods=['GET', 'POST'])
def days(year=datetime.datetime.now().year, month=datetime.datetime.now().month):
    match_doc = {'$match': {'year': year, 'month': month}}
    group_doc = {'$group': {
        '_id': {'day': '$day'},
        'register_count': {'$sum': '$register_count'},
        'authorize_count': {'$sum': '$authorize_count'},}}
    project_doc = {'$project': {
        'day': '$_id.day',
        'register_count': 1,
        'authorize_count': 1,
        '_id': 0}}

    aggregate_list = list()
    aggregate_list.append(match_doc)
    aggregate_list.append(group_doc)
    aggregate_list.append(project_doc)
    ret = CityStatistic.objects().aggregate(*aggregate_list)

    return json.dumps(ret)


@blueprint_main.route('/regions/', methods=['GET', 'POST'])
def regions():
    group_region_doc = {'$group': {
        '_id': {'city': '$city'},
        'count': {'$sum': '$register_count'}}}
    project_region_doc = {'$project': {
        'role': '$_id.city',
        'count': 1,
        '_id': 0}}
    aggregate_list = list()
    aggregate_list.append(group_region_doc)
    aggregate_list.append(project_region_doc)
    ret = CityStatistic.objects().aggrate(*aggregate_list)
    return json.dumps(ret)



