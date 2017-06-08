from . import mongodb
from . import OpenClass


class OpenClassLog(mongodb.Document):
    open_class = mongodb.ReferenceField(OpenClass)

    year = mongodb.IntField()
    month = mongodb.IntField()
    day = mongodb.IntField()

    visit_count = mongodb.IntField()
    display_count = mongodb.IntField()
    comment_count = mongodb.IntField()
    handout_download_count = mongodb.IntField()

    meta = {'collection': 'open_class_logs'}

