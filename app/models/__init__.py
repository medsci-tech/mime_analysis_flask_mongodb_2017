from flask_mongoengine import MongoEngine
mongodb = MongoEngine()

# import your models here,
# otherwise, your models won't be detected by migrate.
from .user import User
from .common_statistic import CommonStatistic
from .doctor import Hospital
from .doctor import Doctor
