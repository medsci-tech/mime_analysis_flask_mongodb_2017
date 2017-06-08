from . import mongodb


class OpenClassUnit(mongodb.Document):
    unit_name = mongodb.StringField()
    disease_label = mongodb.StringField()
    hard_level = mongodb.StringField()
    interest_label_list = mongodb.ListField(mongodb.StringField())

    year = mongodb.IntField()
    month = mongodb.IntField()
    day = mongodb.IntField()

    visit_count = mongodb.IntField()
    display_count = mongodb.IntField()
    consultation_count = mongodb.IntField()
    comment_count = mongodb.IntField()
    # no score.
    order_count = mongodb.IntField()
    income_amount = mongodb.DecimalField()
    ppt_download_count = mongodb.IntField()

    meta = {'collection': 'open_class_units'}

