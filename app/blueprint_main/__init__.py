from flask import Blueprint

blueprint_main = Blueprint('blueprint_main',
                           __name__,
                           url_prefix='/main',
                           template_folder='../templates/main')

from . import views
