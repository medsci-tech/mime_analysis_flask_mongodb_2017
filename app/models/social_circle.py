from . import mongodb
from . import Doctor


class SocialCircle(mongodb.Document):
    doctor = mongodb.ReferenceField(Doctor)
    circle_name = mongodb.StringField()

    year = mongodb.IntField()
    month = mongodb.IntField()
    day = mongodb.IntField()

    member_count = mongodb.IntField()
    topic_count = mongodb.IntField()
    comment_count = mongodb.IntField()

    meta = {'collection': 'social_circles'}

