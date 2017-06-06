from . import mongodb


class Hospital(mongodb.Document):
    name = mongodb.StringField(required=False)
    level = mongodb.StringField(required=False)
    province = mongodb.StringField(required=True)
    city = mongodb.StringField(required=False)
    longitude = mongodb.FloatField(required=False)
    latitude = mongodb.FloatField(required=False)

    meta = {'collection': 'hospitals'}


class Doctor(mongodb.DynamicDocument):
    name = mongodb.StringField(required=False)
    phone = mongodb.StringField(required=True, unique=True)
    age_group = mongodb.StringField(required=False)
    disease_list = mongodb.ListField(required=False)

    province = mongodb.StringField(required=True)
    city = mongodb.StringField(required=False)
    longitude = mongodb.FloatField(required=False)
    latitude = mongodb.FloatField(required=False)

    register_year = mongodb.IntField(required=False)
    register_month = mongodb.IntField(required=False)
    register_day = mongodb.IntField(required=False)

    doctor_title = mongodb.StringField(required=False)
    doctor_office = mongodb.StringField(required=False)
    hospital = mongodb.ReferenceField(Hospital)

    meta = {'collection': 'doctors'}
