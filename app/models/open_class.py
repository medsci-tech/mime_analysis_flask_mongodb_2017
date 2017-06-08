from . import mongodb


class OpenClass(mongodb.Document):
    unit_name = mongodb.StringField()
    class_name = mongodb.StringField()

    visit_count = mongodb.IntField()
    display_count = mongodb.IntField()

    meta = {'collection': 'open_classes'}

