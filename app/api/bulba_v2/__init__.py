from flask import Blueprint, jsonify, request

from app.utils import parse_html_to_md
from app.utils.v2.oai import (
    code_related_and_category_and_complex,
    truthful_and_correct,
    safe_and_harmless,
    sxs,
)

bulba_v2_api_blueprint = Blueprint('bulba_v2_api', __name__)


@bulba_v2_api_blueprint.post('')
def bulba_v2_determine():
    prompt, response_a, response_b = [
        parse_html_to_md(request.form.get(key))
        for key in ['prompt', 'response_a', 'response_b']
    ]
    return jsonify({
        "category": code_related_and_category_and_complex(prompt),
        "truthful_and_correct": truthful_and_correct(prompt, response_a, response_b),
        "safe_and_harmless": safe_and_harmless(prompt, response_a, response_b),
        "sxs": sxs(prompt, response_a, response_b),
    })
