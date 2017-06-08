from . import mongodb


class LiveShow(mongodb.Document):
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

    meta = {'collection': 'live_show'}

