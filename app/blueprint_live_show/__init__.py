from flask import Blueprint

blueprint_live_show = Blueprint('blueprint_live_show',
                           __name__,
                           url_prefix='/live_show',
                           template_folder='../templates/live_show')

from . import views

