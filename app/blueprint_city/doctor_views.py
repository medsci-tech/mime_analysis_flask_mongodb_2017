import json
import datetime
from flask import render_template

from . import blueprint_city
from ..models import Doctor
from ..models import CityStatistic


@blueprint_city.route('/<string:province>')
@blueprint_city.route('/index/<string:province>')
def index(province):
    register_count = CityStatistic.objects(province=province).sum('register_count')
    authorize_count = CityStatistic.objects(province=province).sum('authorize_count')
    ret = {'register_count': register_count, 'authorize_count': authorize_count,}
    render_template('city/city.html', ret=ret)


@blueprint_city.route('/titles/<string:province>', methods=['GET', 'POST'])
def titles(province):
    match_doc = {'$match': {'province': province}}
    group_doc = {'$group': {
        '_id': {'doctor_title': '$doctor_title'},
        'count': {'$sum': 1}}}
    project_doc = {'$project': {
        'doctor_title': '$_id.doctor_title',
        'count': 1,
        '_id': 0}}
    aggregate_list = list()
    aggregate_list.append(match_doc)
    aggregate_list.append(group_doc)
    aggregate_list.append(project_doc)
    ret = Doctor.objects().aggrate(*aggregate_list)
    return json.dumps(ret)


@blueprint_city.route('/offices/<string:province>', methods=['GET', 'POST'])
def offices(province):
    match_doc = {'$match': {'province': province}}
    group_doc = {'$group': {
        '_id': {'doctor_office': '$doctor_office'},
        'count': {'$sum': 1}}}
    project_doc = {'$project': {
        'doctor_office': '$_id.doctor_office',
        'count': 1,
        '_id': 0}}
    aggregate_list = list()
    aggregate_list.append(match_doc)
    aggregate_list.append(group_doc)
    aggregate_list.append(project_doc)
    ret = Doctor.objects().aggrate(*aggregate_list)
    return json.dumps(ret)


@blueprint_city.route('/age_groups/<string:province>', methods=['GET', 'POST'])
def age_groups(province):
    match_doc = {'$match': {'province': province}}
    group_doc = {'$group': {
        '_id': {'age_group': '$age_group'},
        'count': {'$sum': 1}}}
    project_doc = {'$project': {
        'age_group': '$_id.age_group',
        'count': 1,
        '_id': 0}}
    aggregate_list = list()
    aggregate_list.append(match_doc)
    aggregate_list.append(group_doc)
    aggregate_list.append(project_doc)
    ret = Doctor.objects().aggrate(*aggregate_list)
    return json.dumps(ret)

