from . import mongodb


class OpenClassUnit(mongodb.Document):
    unit_name = mongodb.StringField()
    disease_label = mongodb.StringField()
    hard_level = mongodb.StringField()
    interest_label_list = mongodb.ListField(mongodb.StringField())

    visit_count = mongodb.IntField()
    display_count = mongodb.IntField()
    consultation_count = mongodb.IntField()
    class_comment_count = mongodb.IntField()
    score_count = mongodb.IntField()
    purchase_count = mongodb.IntField()
    income_amount = mongodb.DecimalField()
    class_handout_download_count = mongodb.IntField()

    meta = {'collection': 'open_class_units'}

