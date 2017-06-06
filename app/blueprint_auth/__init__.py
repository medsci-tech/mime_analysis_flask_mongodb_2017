from flask import Blueprint

blueprint_auth = Blueprint('blueprint_auth',
                           __name__,
                           url_prefix='/auth',
                           template_folder='../templates/auth')

from . import views
