from . import mongodb


class OpenClass(mongodb.Document):
    unit_name = mongodb.StringField()
    class_name = mongodb.StringField()
    disease_label = mongodb.StringField()
    hard_level = mongodb.StringField()
    interest_label_list = mongodb.ListField(mongodb.StringField())

    visit_count = mongodb.IntField()
    display_count = mongodb.IntField()
    comment_count = mongodb.IntField()
    score_count = mongodb.IntField()
    handout_download_count = mongodb.IntField()

    meta = {'collection': 'open_classes'}

