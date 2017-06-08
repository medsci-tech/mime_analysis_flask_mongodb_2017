import json

from . import blueprint_main
from ..models import CityStatistic


@blueprint_main.route('/regions/', methods=['GET', 'POST'])
def regions():
    group_region_doc = {'$group': {
        '_id': {'city': '$city',
                'longitude': '$longitude',
                'latitude': '$latitude'},
        'count': {'$sum': '$register_count'}}}
    project_region_doc = {'$project': {
        'city': '$_id.city',
        'longitude': '$_id.longitude',
        'latitude': '$_id.latitude',
        'count': 1,
        '_id': 0}}
    aggregate_list = list()
    aggregate_list.append(group_region_doc)
    aggregate_list.append(project_region_doc)
    ret = CityStatistic.objects().aggregate(*aggregate_list)
    print(list(ret))
    return json.dumps(list(ret))

