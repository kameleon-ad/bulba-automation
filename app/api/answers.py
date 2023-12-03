from flask import Blueprint, jsonify, request

from app.models import Answer, Response, Prompt, Question
from app.utils import parse_bulba_request, parse_html_to_md
from app.utils.db import *
from app.utils.string import strip_prompt, normalize_question, strip_response

answers_api_blueprint = Blueprint('answers-api', __name__)


@answers_api_blueprint.get('')
def retrieve_answers():
    answers = [answer.to_dict() for answer in Answer.query.all()]
    return jsonify(answers)


@answers_api_blueprint.post('')
def create_answer():
    answer = request.form.get('answer').strip()
    if prompt_id := request.form.get('prompt_id') is None:
        if prompt := request.form.get('prompt'):
            if prompt := get_create(Prompt, prompt=parse_html_to_md(prompt).strip()):
                prompt_id = prompt.id

    if response_id := request.form.get('response_id') is None:
        if response := request.form.get('response'):
            if response := get_create(
                Response,
                response=strip_response(parse_html_to_md(response)),
                prompt_id=prompt_id,
            ):
                response_id = response.id
    # correct = request.form.get('correct')
    question = request.form.get('question')
    question = normalize_question(question)
    print(question)
    question_id = get_create(Question, question=question).id

    if answer == 'n_a':
        answer = 'N/A'
    if answer.isnumeric():
        answer = {
            "1": "Too Verbose",
            "2": "Just Right",
            "3": "Too Short",
        }[answer]

    if exists(Answer, correct=True, answer=answer, question_id=question_id, response_id=response_id):
        return jsonify({'answer': f'The answer already exists.'}), 409

    create(Answer, correct=True, answer=answer, question_id=question_id, response_id=response_id)
    return {'success': True}


@answers_api_blueprint.get('/<int:rid>')
def retrieve_answer(rid: int):
    answer = Answer.query.get(rid)
    if not answer:
        return jsonify({"answer": f"There is not any answer with id-{rid}"}), 404
    return jsonify(answer.to_dict())
