from . import mongodb
from . import OpenClassUnit


class OpenClassUnitLog(mongodb.Document):
    open_class_unit = mongodb.ReferenceField(OpenClassUnit)

    year = mongodb.IntField()
    month = mongodb.IntField()
    day = mongodb.IntField()

    visit_count = mongodb.IntField()
    display_count = mongodb.IntField()
    consultation_count = mongodb.IntField()
    class_comment_count = mongodb.IntField()
    # no score.
    purchase_count = mongodb.IntField()
    income_amount = mongodb.DecimalField()
    class_handout_download_count = mongodb.IntField()

    meta = {'collection': 'open_class_units'}

