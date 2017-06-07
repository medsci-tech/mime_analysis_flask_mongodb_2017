from . import mongodb
from . import City


class CityStatistic(mongodb.Document):
    city = mongodb.ReferenceField(City)

    year = mongodb.IntField(required=False)
    month = mongodb.IntField(required=False)
    day = mongodb.IntField(required=False)

    register_count = mongodb.IntField(required=False)
    authorize_count = mongodb.IntField(required=False)

    meta = {'collection': 'city_statistics'}

