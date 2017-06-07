import json
from flask import render_template

from . import blueprint_main
from ..models import Doctor


@blueprint_main.route('/')
@blueprint_main.route('/index/')
def index():
    register_count = Doctor.objects.count()
    authorize_count = Doctor.objects(__raw__={'id_num': {'$exists': True}}).count()
    ret = {'register_count': register_count, 'authorize_count': authorize_count,}
    render_template('main/main.html', statistic_info=ret)


@blueprint_main.route('/titles/', methods=['GET', 'POST'])
def titles():
    group_region_doc = {'$group': {
        '_id': {'doctor_title': '$doctor_title'},
        'count': {'$sum': 1}}}
    project_region_doc = {'$project': {
        'doctor_title': '$_id.doctor_title',
        'count': 1,
        '_id': 0}}
    aggregate_list = list()
    aggregate_list.append(group_region_doc)
    aggregate_list.append(project_region_doc)
    ret = Doctor.objects().aggrate(*aggregate_list)
    return json.dumps(ret)


@blueprint_main.route('/offices/', methods=['GET', 'POST'])
def offices():
    group_region_doc = {'$group': {
        '_id': {'doctor_office': '$doctor_office'},
        'count': {'$sum': 1}}}
    project_region_doc = {'$project': {
        'doctor_office': '$_id.doctor_office',
        'count': 1,
        '_id': 0}}
    aggregate_list = list()
    aggregate_list.append(group_region_doc)
    aggregate_list.append(project_region_doc)
    ret = Doctor.objects().aggrate(*aggregate_list)
    return json.dumps(ret)


@blueprint_main.route('/age_groups/', methods=['GET', 'POST'])
def age_groups():
    group_region_doc = {'$group': {
        '_id': {'age_group': '$age_group'},
        'count': {'$sum': 1}}}
    project_region_doc = {'$project': {
        'age_group': '$_id.age_group',
        'count': 1,
        '_id': 0}}
    aggregate_list = list()
    aggregate_list.append(group_region_doc)
    aggregate_list.append(project_region_doc)
    ret = Doctor.objects().aggrate(*aggregate_list)
    return json.dumps(ret)

