from . import mongodb


class OpenclassStatistic(mongodb.Document):
    year = mongodb.IntField()
    month = mongodb.IntField()
    day = mongodb.IntField()

    unit_name = mongodb.StringField()
    class_name = mongodb.StringField()
    visit_count = mongodb.IntField()
    purchase_count = mongodb.IntField()
    view_count = mongodb.IntField()

    meta = {'collection': 'openclass_statistics'}

