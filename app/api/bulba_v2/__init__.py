from flask import Blueprint, jsonify, request

from app.utils import parse_html_to_md
from app.utils.v2.oai import category

bulba_v2_api_blueprint = Blueprint('bulba_v2_api', __name__)


@bulba_v2_api_blueprint.post('')
def bulba_v2_determine():
    prompt, response_a, response_b = [
        parse_html_to_md(request.form.get(key))
        for key in ['prompt', 'response_a', 'response_b']
    ]
    return jsonify({
        "category": category(prompt),
    })
