from flask import Blueprint, jsonify, request

from app.extension import SQL_DB
from app.models import Question

questions_api_blueprint = Blueprint('questions-api', __name__)


@questions_api_blueprint.get('')
def retrieve_questions():
    questions = [
        {'id': qid, 'question': question}
        for qid, question in Question.query.with_entities(Question.id, Question.question).all()
    ]
    return jsonify(questions)


@questions_api_blueprint.post('')
def create_question():
    question = request.form.get('question')
    instruction = request.form.get('instruction')
    exists = SQL_DB.session.query(
        Question.query.filter_by(question=question).exists()
    ).scalar()
    if exists:
        return jsonify({'question': f'The question already exists.'}), 409
    Question.create(question, instruction)
    return {'success': True}


@questions_api_blueprint.get('/<int:qid>')
def retrieve_question(qid: int):
    question = Question.query.get(qid)
    return jsonify(question.to_dict())
