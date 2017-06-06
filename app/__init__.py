from flask import Flask

from .config import configs
from .vendors import bcrypt

from .blueprint_auth import blueprint_auth


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(configs[config_name])

    # init vendors here.
    bcrypt.init_app(app)

    # register blueprints here.
    app.register_blueprint(blueprint_auth)

    return app
