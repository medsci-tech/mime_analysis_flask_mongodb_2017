from flask import Blueprint

blueprint_main = Blueprint('blueprint_main',
                           __name__,
                           url_prefix='/main',
                           template_folder='../templates/main')

from . import doctor_views
from . import region_views
from . import time_views

