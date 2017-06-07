from flask_mongoengine import MongoEngine

mongodb = MongoEngine()

# import your models here,
# otherwise, your models won't be detected by migrate.
from .user import User
from .city_statistics import CityStatistic
from .doctor import Doctor

