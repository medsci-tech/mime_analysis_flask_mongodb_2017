from . import mongodb


class CityStatistic(mongodb.Document):
    province = mongodb.StringField(required=True)
    city = mongodb.StringField(required=False)
    longitude = mongodb.FloatField(required=False)
    latitude = mongodb.FloatField(required=False)

    year = mongodb.IntField(required=False)
    month = mongodb.IntField(required=False)
    day = mongodb.IntField(required=False)

    register_count = mongodb.IntField(required=False)
    authorize_count = mongodb.IntField(required=False)
    live_count = mongodb.IntField(required=False)
    open_class_count = mongodb.IntField(required=False)
    social_circle_count = mongodb.IntField(required=False)

    meta = {'collection': 'city_statistics'}

