from flask import Blueprint, jsonify, request

from app.models import Prompt
from app.utils.db import *

prompts_api_blueprint = Blueprint('prompts-api', __name__)


@prompts_api_blueprint.get('')
def retrieve_prompts():
    prompts = [prompt.to_dict() for prompt in Prompt.query.all()]
    return jsonify(prompts)


@prompts_api_blueprint.post('')
def create_prompt():
    prompt = request.form.get('prompt')

    if exists(Prompt, prompt=prompt):
        return jsonify({'prompt': f'The prompt already exists.'}), 409

    create(Prompt, prompt=prompt)
    return {'success': True}


@prompts_api_blueprint.get('/<int:pid>')
def retrieve_prompt(pid: int):
    prompt = Prompt.query.get(pid)
    return jsonify(prompt.to_dict())
