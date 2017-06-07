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
        'role': '$_id.city',
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

