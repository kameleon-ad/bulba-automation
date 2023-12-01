from flask import Blueprint, jsonify, request

from app.models import Response
from app.utils.db import *

responses_api_blueprint = Blueprint('responses-api', __name__)


@responses_api_blueprint.get('')
def retrieve_responses():
    responses = [response.to_dict() for response in Response.query.all()]
    return jsonify(responses)


@responses_api_blueprint.post('')
def create_response():
    response = request.form.get('response')
    prompt = request.form.get('prompt')

    if exists(Response, response=response, prompt_id=prompt):
        return jsonify({'response': f'The response already exists.'}), 409

    create(Response, response=response, prompt_id=prompt)
    return {'success': True}


@responses_api_blueprint.get('/<int:rid>')
def retrieve_response(rid: int):
    response = Response.query.get(rid)
    return jsonify(response.to_dict())
