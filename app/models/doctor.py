from . import mongodb
from . import City
from . import Hospital


class Doctor(mongodb.DynamicDocument):
    name = mongodb.StringField(required=False)
    phone = mongodb.StringField(required=True, unique=True)
    age_group = mongodb.StringField(required=False)
    disease_list = mongodb.ListField(required=False)

    register_year = mongodb.IntField(required=False)
    register_month = mongodb.IntField(required=False)
    register_day = mongodb.IntField(required=False)

    doctor_title = mongodb.StringField(required=False)
    doctor_office = mongodb.StringField(required=False)

    city = mongodb.ReferenceField(City)
    hospital = mongodb.ReferenceField(Hospital)

    meta = {'collection': 'doctors'}
