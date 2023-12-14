from flask import Blueprint, jsonify

from .answers import answers_api_blueprint
from .bulba import bulba_api_blueprint
from .bulba_v2 import bulba_v2_api_blueprint
from .bulba_v3 import bulba_v3_api_blueprint
from .htmls import htmls_api_blueprint
from .prompts import prompts_api_blueprint
from .questions import questions_api_blueprint
from .responses import responses_api_blueprint
from .samples import samples_api_blueprint

api_blueprint = Blueprint('api', __name__)
api_blueprint.register_blueprint(answers_api_blueprint, url_prefix='/answers')
api_blueprint.register_blueprint(bulba_api_blueprint, url_prefix='/bulba')
api_blueprint.register_blueprint(bulba_v2_api_blueprint, url_prefix='/bulba_v2')
api_blueprint.register_blueprint(bulba_v3_api_blueprint, url_prefix='/bulba_v3')
api_blueprint.register_blueprint(htmls_api_blueprint, url_prefix='/htmls')
api_blueprint.register_blueprint(prompts_api_blueprint, url_prefix='/prompts')
api_blueprint.register_blueprint(questions_api_blueprint, url_prefix='/questions')
api_blueprint.register_blueprint(responses_api_blueprint, url_prefix='/responses')
api_blueprint.register_blueprint(samples_api_blueprint, url_prefix='/samples')


@api_blueprint.get('/health')
def api_health():
    return jsonify({'status': 'UP'})
