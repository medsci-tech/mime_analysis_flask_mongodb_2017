import datetime
from . import mongodb
from ..vendors import bcrypt


class User(mongodb.Document):
    phone = mongodb.StringField(required=True)
    sms_code = mongodb.StringField(required=False)
    password = mongodb.StringField(required=False)
    updated_at = mongodb.DateTimeField(default=datetime.datetime.now())

    meta = {'collection': 'users'}

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password)

    def check_password(self, password):
        ret = bcrypt.check_password_hash(self.password, password)
        return ret

