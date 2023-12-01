from flask import Blueprint, jsonify

from .bulba import bulba_api_blueprint
from .htmls import htmls_api_blueprint
from .questions import questions_api_blueprint

api_blueprint = Blueprint('api', __name__)
api_blueprint.register_blueprint(bulba_api_blueprint, url_prefix='/bulba')
api_blueprint.register_blueprint(htmls_api_blueprint, url_prefix="/htmls")
api_blueprint.register_blueprint(questions_api_blueprint, url_prefix="/questions")


@api_blueprint.get('/health')
def api_health():
    return jsonify({"status": "UP"})
