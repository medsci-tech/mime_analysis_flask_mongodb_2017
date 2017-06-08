from flask import Blueprint

blueprint_open_class = Blueprint('blueprint_open_class',
                           __name__,
                           url_prefix='/open_class',
                           template_folder='../templates/open_class')

from . import views

