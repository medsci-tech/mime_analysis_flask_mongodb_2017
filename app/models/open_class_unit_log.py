from . import mongodb
from . import OpenClassUnit


class OpenClassUnitLog(mongodb.Document):
    open_class_unit = mongodb.ReferenceField(OpenClassUnit)
    year = mongodb.IntField()
    month = mongodb.IntField()
    day = mongodb.IntField()

