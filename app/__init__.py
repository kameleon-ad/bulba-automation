from flask import Flask
from flask_cors import CORS

from app.api import api_blueprint
from app.config import DevelopmentConfig
from app.extension import SQL_DB


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)

    CORS(app)
    SQL_DB.init_app(app)

    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app
