from flask import Blueprint, jsonify

from ..utils import parse_bulba_request
from ..utils.openai import DEFAULT_PROMPTS, OPENAI_CLIENT

bulba_api_blueprint = Blueprint('bulba-api', __name__)


@bulba_api_blueprint.post("/openai")
def bulba_openai():
    _, instruction, prompt, response_a, response_b = parse_bulba_request()
    print(prompt)
    return jsonify({"success": True})


@bulba_api_blueprint.get("/default-prompts")
def bulba_default_prompts():
    res = OPENAI_CLIENT.chat.completions.create(
        model="gpt-4",
        messages=DEFAULT_PROMPTS,
    )
    print(res.choices[0].message.content)
    return jsonify(DEFAULT_PROMPTS)
