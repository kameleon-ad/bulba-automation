from flask import Blueprint, jsonify, request

from app.utils import parse_html_to_md
from app.utils.v2.oai import code_related_and_category, truthful_and_correct

bulba_v2_api_blueprint = Blueprint('bulba_v2_api', __name__)


@bulba_v2_api_blueprint.post('')
def bulba_v2_determine():
    prompt, response_a, response_b = [
        parse_html_to_md(request.form.get(key))
        for key in ['prompt', 'response_a', 'response_b']
    ]
    return jsonify({
        "category": code_related_and_category(prompt),
        "truthful_and_correct": truthful_and_correct(prompt, response_a, response_b),
    })
