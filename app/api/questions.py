from flask import Blueprint, jsonify, request

from app.models import Question
from app.utils.db import *

questions_api_blueprint = Blueprint('questions-api', __name__)


@questions_api_blueprint.get('')
def retrieve_questions():
    questions = [question.to_dict() for question in Question.query.all()]
    return jsonify(questions)


@questions_api_blueprint.post('')
def create_question():
    question = request.form.get('question')
    instruction = request.form.get('instruction')

    if exists(Question, question=question):
        return jsonify({'question': f'The question already exists.'}), 409

    Question.create(question, instruction)
    return {'success': True}


@questions_api_blueprint.get('/<int:qid>')
def retrieve_question(qid: int):
    question = Question.query.get(qid)
    return jsonify(question.to_dict())
