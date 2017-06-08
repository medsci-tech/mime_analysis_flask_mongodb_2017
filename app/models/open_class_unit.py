from . import mongodb


class OpenClassUnit(mongodb.Document):
    unit_name = mongodb.StringField()
    visit_count = mongodb.IntField()
    display_count = mongodb.IntField()
    purchase_count = mongodb.IntField()
    income_amount = mongodb.DecimalField()

    meta = {'collection': 'open_class_units'}

