from flask import Blueprint, jsonify, request

from app.models import Question
from app.utils.db import *
from app.utils.string import normalize_question

questions_api_blueprint = Blueprint('questions-api', __name__)


@questions_api_blueprint.get('')
def retrieve_questions():
    questions = [question.to_dict() for question in Question.query.all()]
    return jsonify(questions)


@questions_api_blueprint.post('')
def create_question():
    question = request.form.get('question')
    instruction = request.form.get('instruction', '')
    question = normalize_question(question)

    if exists(Question, question=question):
        return jsonify({'question': f'The question already exists.'}), 409

    create(Question, question=question, instruction=instruction)
    return {'success': True}


@questions_api_blueprint.get('/<int:qid>')
def retrieve_question(qid: int):
    question = Question.query.get(qid)
    return jsonify(question.to_dict())
