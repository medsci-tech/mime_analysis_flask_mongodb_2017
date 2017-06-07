import json

from . import blueprint_city
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
    ret = CityStatistic.objects().aggrate(*aggregate_list)
    return json.dumps(ret)


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
    aggregate_list = list()
    aggregate_list.append(match_doc)
    aggregate_list.append(group_doc)
    aggregate_list.append(project_doc)
    ret = CityStatistic.objects().aggrate(*aggregate_list)
    return json.dumps(ret)


@blueprint_city.route('/hospitals/<string:province>', methods=['GET', 'POST'])
def hospitals(province):
    pass




