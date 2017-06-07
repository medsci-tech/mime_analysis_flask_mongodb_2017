from . import mongodb
from . import City


class Hospital(mongodb.Document):
    name = mongodb.StringField(required=False)
    level = mongodb.StringField(required=False)
    city = mongodb.ReferenceField(City)

    meta = {'collection': 'hospitals'}
