from . import mongodb


class OpenClass(mongodb.Document):
    unit_name = mongodb.StringField()
    class_name = mongodb.StringField()
    visit_count = mongodb.IntField()
    purchase_count = mongodb.IntField()
    display_count = mongodb.IntField()

    meta = {'collection': 'open_class_statistics'}


class OpenClassLog(mongodb.Document):
    year = mongodb.IntField()
    month = mongodb.IntField()
    day = mongodb.IntField()

