from flask import Blueprint, jsonify

from .bulba import bulba_api_blueprint

api_blueprint = Blueprint('api', __name__)
api_blueprint.register_blueprint(bulba_api_blueprint, url_prefix='/bulba')


@api_blueprint.get('/health')
def api_health():
    return jsonify({"status": "UP"})
