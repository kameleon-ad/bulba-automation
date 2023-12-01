from flask import Blueprint, jsonify, request

from app.extension import SQL_DB
from app.models import Response

responses_api_blueprint = Blueprint('responses-api', __name__)


@responses_api_blueprint.get('')
def retrieve_responses():
    responses = [
        {'id': rid, 'response': response}
        for rid, response in Response.query.with_entities(Response.id, Response.response).all()
    ]
    return jsonify(responses)


@responses_api_blueprint.post('')
def create_response():
    response = request.form.get('response')
    prompt = request.form.get('prompt')
    exists = SQL_DB.session.query(
        Response.query.filter_by(response=response).exists()
    ).scalar()
    if exists:
        return jsonify({'response': f'The response already exists.'}), 409
    Response.create(response, prompt)
    return {'success': True}


@responses_api_blueprint.get('/<int:rid>')
def retrieve_response(rid: int):
    response = Response.query.get(rid)
    return jsonify(response.to_dict())
