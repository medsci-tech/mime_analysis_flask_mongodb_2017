from flask import Blueprint


blueprint_city = Blueprint('blueprint_city',
                           __name__,
                           url_prefix='/city',
                           template_folder='../templates/city')

from . import doctor_views
from . import region_views
from . import time_views

