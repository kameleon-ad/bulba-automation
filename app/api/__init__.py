from flask import Blueprint, jsonify

from .bulba import bulba_api_blueprint
from .html import html_api_blueprint

api_blueprint = Blueprint('api', __name__)
api_blueprint.register_blueprint(bulba_api_blueprint, url_prefix='/bulba')
api_blueprint.register_blueprint(html_api_blueprint, url_prefix="/html")


@api_blueprint.get('/health')
def api_health():
    return jsonify({"status": "UP"})
