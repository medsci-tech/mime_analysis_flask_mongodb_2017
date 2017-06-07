import datetime
import json

from . import blueprint_main
from ..models import CityStatistic


@blueprint_main.route('/months/<int:year>', methods=['GET', 'POST'])
def months(year=datetime.datetime.now().year):
    pass


@blueprint_main.route('/days/<int:year>/<int:month>', methods=['GET', 'POST'])
def days(year=datetime.datetime.now().year, month=datetime.datetime.now().month):
    pass


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



