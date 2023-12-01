from flask import Blueprint, jsonify, request

from app.extension import SQL_DB
from app.models import Prompt

prompts_api_blueprint = Blueprint('prompts-api', __name__)


@prompts_api_blueprint.get('')
def retrieve_prompts():
    prompts = [
        {'id': pid, 'prompt': prompt}
        for pid, prompt in Prompt.query.with_entities(Prompt.id, Prompt.prompt).all()
    ]
    return jsonify(prompts)


@prompts_api_blueprint.post('')
def create_prompt():
    prompt = request.form.get('prompt')
    instruction = request.form.get('instruction')
    exists = SQL_DB.session.query(
        Prompt.query.filter_by(prompt=prompt).exists()
    ).scalar()
    if exists:
        return jsonify({'prompt': f'The prompt already exists.'}), 409
    Prompt.create(prompt, instruction)
    return {'success': True}


@prompts_api_blueprint.get('/<int:pid>')
def retrieve_prompt(pid: int):
    prompt = Prompt.query.get(pid)
    return jsonify(prompt.to_dict())
