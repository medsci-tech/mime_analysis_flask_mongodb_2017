import json

from . import blueprint_main
from ..models import CityStatistic


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



