from . import mongodb
from . import Doctor


class OpenClass(mongodb.Document):
    doctor = mongodb.ReferenceField(Doctor)

    unit_name = mongodb.StringField()
    class_name = mongodb.StringField()
    disease_label = mongodb.StringField()
    hard_level = mongodb.StringField()
    interest_label_list = mongodb.ListField(mongodb.StringField())

    year = mongodb.IntField()
    month = mongodb.IntField()
    day = mongodb.IntField()

    visit_count = mongodb.IntField()
    display_count = mongodb.IntField()
    comment_count = mongodb.IntField()
    # no score.
    ppt_download_count = mongodb.IntField()

    meta = {'collection': 'open_classes'}

