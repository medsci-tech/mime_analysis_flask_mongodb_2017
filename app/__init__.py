from flask import Flask

from .models import mongodb
from .config import configs
from .vendors import bcrypt

from .blueprint_auth import blueprint_auth
from .blueprint_time import blueprint_time


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(configs[config_name])

    # init vendors here.
    mongodb.init_app(app)
    bcrypt.init_app(app)

    # register blueprints here.
    app.register_blueprint(blueprint_auth)
    app.register_blueprint(blueprint_time)

    return app
