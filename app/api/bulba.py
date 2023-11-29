from flask import Blueprint, jsonify

from ..utils import parse_bulba_request

bulba_api_blueprint = Blueprint('bulba-api', __name__)


@bulba_api_blueprint.post("/openai")
def bulba_openai():
    _, instruction, prompt, response_a, response_b = parse_bulba_request()
    print(prompt)
    return jsonify({"success": True})
