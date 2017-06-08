from flask_mongoengine import MongoEngine

mongodb = MongoEngine()

# import your models here,
# otherwise, your models won't be detected by migrate.
from .user import User
from .city_statistic import CityStatistic
from .open_class_unit import OpenClassUnit
from .open_class import OpenClass
from.open_class_unit_log import OpenClassUnitLog

