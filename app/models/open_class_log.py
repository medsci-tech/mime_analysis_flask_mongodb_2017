from . import mongodb
from . import OpenClass


class OpenClassLog(mongodb.Document):
    open_class = mongodb.ReferenceField(OpenClass)

    year = mongodb.IntField()
    month = mongodb.IntField()
    day = mongodb.IntField()

