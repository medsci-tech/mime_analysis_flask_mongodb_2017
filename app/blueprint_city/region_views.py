import json

from . import blueprint_city
from ..models import Doctor
from ..models import CityStatistic


@blueprint_city.route('/regions/<string:province>', methods=['GET', 'POST'])
def regions(province):
    match_doc = {'$match': {'province': province}}
    group_doc = {'$group': {
        '_id': {'city': '$city',
                'longitude': '$longitude',
                'latitude': '$latitude'},
        'count': {'$sum': '$register_count'}}}
    project_doc = {'$project': {
        'city': '$_id.city',
        'longitude': '$_id.longitude',
        'latitude': '$_id.latitude',
        'count': 1,
        '_id': 0}}
    aggregate_list = list()
    aggregate_list.append(match_doc)
    aggregate_list.append(group_doc)
    aggregate_list.append(project_doc)
    ret = CityStatistic.objects().aggregate(*aggregate_list)
    print(list(ret))
    return json.dumps(list(ret))


@blueprint_city.route('/cities/<string:province>', methods=['GET', 'POST'])
def cities(province):
    match_doc = {'$match': {'province': province}}
    group_doc = {'$group': {
        '_id': {'city': '$city'},
        'count': {'$sum': '$register_count'}}}
    project_doc = {'$project': {
        'city': '$_id.city',
        'count': 1,
        '_id': 0}}
    sort_doc = {'$sort': {'count': 1}}
    limit_doc = {'$limit': 10}
    aggregate_list = list()
    aggregate_list.append(match_doc)
    aggregate_list.append(group_doc)
    aggregate_list.append(project_doc)
    aggregate_list.append(sort_doc)
    aggregate_list.append(limit_doc)
    ret = CityStatistic.objects().aggregate(*aggregate_list)
    print(list(ret))
    return json.dumps(list(ret))


@blueprint_city.route('/hospitals/<string:province>', methods=['GET', 'POST'])
def hospitals(province):
    match_doc = {'$match': {'province': province}}
    group_doc = {'$group': {
        '_id': {'city': '$city'},
        'count': {'$sum': 1}}}
    project_doc = {'$project': {
        'city': '$_id.city',
        'count': 1,
        '_id': 0}}
    sort_doc = {'$sort': {'count': 1}}
    limit_doc = {'$limit': 10}
    aggregate_list = list()
    aggregate_list.append(match_doc)
    aggregate_list.append(group_doc)
    aggregate_list.append(project_doc)
    aggregate_list.append(sort_doc)
    aggregate_list.append(limit_doc)
    ret = Doctor.objects().aggregate(*aggregate_list)
    print(list(ret))
    return json.dumps(list(ret))

