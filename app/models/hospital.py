from . import mongodb


class Hospital(mongodb.Document):
    name = mongodb.StringField(required=False)
    level = mongodb.StringField(required=False)
    province = mongodb.StringField(required=True)
    city = mongodb.StringField(required=False)
    longitude = mongodb.FloatField(required=False)
    latitude = mongodb.FloatField(required=False)

    meta = {'collection': 'hospitals'}