from flask import Flask, send_from_directory
from flask_cors import CORS

from app.api import api_blueprint
from app.config import DevelopmentConfig
from app.extension import SQL_DB, DB_MIGRATE


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)

    CORS(app)
    SQL_DB.init_app(app)
    DB_MIGRATE.init_app(app, SQL_DB)

    app.register_blueprint(api_blueprint, url_prefix='/api')

    @app.get("/")
    def index():
        return send_from_directory('static', 'index.html')

    return app
