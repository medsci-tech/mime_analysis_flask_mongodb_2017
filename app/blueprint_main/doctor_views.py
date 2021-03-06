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
    print(ret)
    return render_template('main/index.html', ret=ret)


@blueprint_main.route('/titles/', methods=['GET', 'POST'])
def titles():
    group_doc = {'$group': {
        '_id': {'doctor_title': '$doctor_title'},
        'count': {'$sum': 1}}}
    project_doc = {'$project': {
        'doctor_title': '$_id.doctor_title',
        'count': 1,
        '_id': 0}}
    aggregate_list = list()
    aggregate_list.append(group_doc)
    aggregate_list.append(project_doc)
    ret = Doctor.objects().aggregate(*aggregate_list)
    print(list(ret))
    return json.dumps(list(ret))


@blueprint_main.route('/offices/', methods=['GET', 'POST'])
def offices():
    group_doc = {'$group': {
        '_id': {'doctor_office': '$doctor_office'},
        'count': {'$sum': 1}}}
    project_doc = {'$project': {
        'doctor_office': '$_id.doctor_office',
        'count': 1,
        '_id': 0}}
    aggregate_list = list()
    aggregate_list.append(group_doc)
    aggregate_list.append(project_doc)
    ret = Doctor.objects().aggregate(*aggregate_list)
    print(list(ret))
    return json.dumps(list(ret))


@blueprint_main.route('/age_groups/', methods=['GET', 'POST'])
def age_groups():
    group_doc = {'$group': {
        '_id': {'age_group': '$age_group'},
        'count': {'$sum': 1}}}
    project_doc = {'$project': {
        'age_group': '$_id.age_group',
        'count': 1,
        '_id': 0}}
    aggregate_list = list()
    aggregate_list.append(group_doc)
    aggregate_list.append(project_doc)
    ret = Doctor.objects().aggregate(*aggregate_list)
    print(list(ret))
    return json.dumps(list(ret))

