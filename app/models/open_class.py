from . import mongodb


class OpenClassUnit(mongodb.Document):
    unit_name = mongodb.StringField()
    visit_count = mongodb.IntField()
    display_count = mongodb.IntField()
    purchase_count = mongodb.IntField()

    meta = {'collection': 'open_class_units'}


class OpenClass(mongodb.Document):
    unit_name = mongodb.StringField()
    class_name = mongodb.StringField()

    visit_count = mongodb.IntField()
    display_count = mongodb.IntField()
    purchase_count = mongodb.IntField()

    meta = {'collection': 'open_classes'}


class OpenClassUnitLog(mongodb.Document):
    open_class = mongodb.ReferenceField(OpenClass)
    year = mongodb.IntField()
    month = mongodb.IntField()
    day = mongodb.IntField()


class OpenClassLog(mongodb.Document):
    open_class = mongodb.ReferenceField(OpenClass)

    year = mongodb.IntField()
    month = mongodb.IntField()
    day = mongodb.IntField()

