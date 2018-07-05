import os

from flask import Flask
from . import hoge

config = {
    'default': 'config.default',
    'development': 'config.development',
    'production': 'config.production'
}

app = Flask(__name__, instance_relative_config=True)
config_name = os.getenv('FLASK_CONFIGURATION', 'default')
app.config.from_object(config[config_name])
app.config.from_pyfile('application.cfg', silent=True)

blueprints = [hoge]
for blueprint in blueprints:
    app.register_blueprint(blueprint.app)
