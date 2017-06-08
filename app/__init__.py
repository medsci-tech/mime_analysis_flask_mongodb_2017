from flask import Flask

from .models import mongodb
from .config import configs
from .vendors import bcrypt

from .blueprint_auth import blueprint_auth
from .blueprint_main import blueprint_main
from .blueprint_city import blueprint_city
from .blueprint_open_class import blueprint_open_class
from .blueprint_live_show import blueprint_live_show


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(configs[config_name])

    # init vendors here.
    mongodb.init_app(app)
    bcrypt.init_app(app)

    # register blueprints here.
    app.register_blueprint(blueprint_auth)
    app.register_blueprint(blueprint_main)
    app.register_blueprint(blueprint_city)
    app.register_blueprint(blueprint_open_class)
    app.register_blueprint(blueprint_live_show)

    return app

