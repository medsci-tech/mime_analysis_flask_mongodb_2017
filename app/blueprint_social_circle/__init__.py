from flask import Blueprint

blueprint_social_circle = Blueprint('blueprint_social_circle',
                           __name__,
                           url_prefix='/social_circle',
                           template_folder='../templates/social_circle')

from . import views

