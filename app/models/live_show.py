from . import mongodb
from . import Doctor


class LiveShow(mongodb.Document):
    doctor = mongodb.ReferenceField(Doctor)

    show_name = mongodb.StringField()
    show_type = mongodb.StringField()
    show_length = mongodb.IntField()
    disease_label = mongodb.StringField()

    year = mongodb.IntField()
    month = mongodb.IntField()
    day = mongodb.IntField()

    audience_count = mongodb.IntField()
    comment_count = mongodb.IntField()
    score_count = mongodb.IntField()

    meta = {'collection': 'live_shows'}

