from . import mongodb


class CommonStatistic(mongodb.DynamicDocument):
    province = mongodb.StringField(required=True)
    city = mongodb.StringField(required=False)
    longitude = mongodb.FloatField(required=False)
    latitude = mongodb.FloatField(required=False)

    year = mongodb.IntField(required=False)
    month = mongodb.IntField(required=False)
    day = mongodb.IntField(required=False)

    register_count = mongodb.IntField(required=False)
    authorize_count = mongodb.IntField(required=False)
    trade_count = mongodb.IntField(required=False)

    meta = {'collection': 'common_statistics'}
