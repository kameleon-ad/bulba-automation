from flask import Blueprint, jsonify, request

from app.models import Answer
from app.utils.db import *

answers_api_blueprint = Blueprint('answers-api', __name__)


@answers_api_blueprint.get('')
def retrieve_answers():
    answers = [answer.to_dict() for answer in Answer.query.all()]
    return jsonify(answers)


@answers_api_blueprint.post('')
def create_answer():
    answer = request.form.get('answer')
    prompt = request.form.get('prompt')
    correct = request.form.get('correct')

    if exists(Answer, answer=answer, prompt_id=prompt):
        return jsonify({'answer': f'The answer already exists.'}), 409

    create(Answer, answer=answer, prompt_id=prompt, correct=correct)
    return {'success': True}


@answers_api_blueprint.get('/<int:rid>')
def retrieve_answer(rid: int):
    answer = Answer.query.get(rid)
    if not answer:
        return jsonify({"answer": f"There is not any answer with id-{rid}"}), 404
    return jsonify(answer.to_dict())
