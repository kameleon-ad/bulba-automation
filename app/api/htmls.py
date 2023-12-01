from flask import (
    Blueprint,
    jsonify,
)

from app.models import Html, Prompt, Response
from app.utils import parse_bulba_request
from app.utils.db import *

htmls_api_blueprint = Blueprint('htmls-api', __name__)


@htmls_api_blueprint.get("/problems")
def retrieve_problems():
    problems = Html \
        .query \
        .filter_by(problem=True) \
        .all()
    return jsonify([problem.to_dict() for problem in problems])


@htmls_api_blueprint.post("/problems")
def problem_html_upload():
    # noinspection DuplicatedCode
    _, html_content, _, prompt, response_a, response_b = parse_bulba_request()

    if not exists(Prompt, prompt=prompt):
        create(Prompt, prompt=prompt)

    prompt_id = Prompt.query.filter_by(prompt=prompt).first().id

    if not exists(Response, response=response_a, prompt_id=prompt_id):
        create(Response, response=response_a, prompt_id=prompt_id)

    if not exists(Response, response=response_b, prompt_id=prompt_id):
        create(Response, response=response_b, prompt_id=prompt_id)

    if exists(Html, content=html_content, problem=True):
        return jsonify({"html": f"The problem already exists."}), 409
    create(Html, problem=True, content=html_content)

    return jsonify({"success": True})


@htmls_api_blueprint.get("/problems/<int:pk>")
def retrieve_problem(pk: int):
    html = Html.query.get(pk)
    if not html:
        return jsonify({"status": f"Not able to find the Html-{pk}."}), 404
    if not html.problem:
        return jsonify({"status": f"The Html-{pk} is not problem."}), 404
    return html.to_dict()


@htmls_api_blueprint.delete("/problems/<string:pk>")
def delete_problem(pk: str):
    delete(Html, id=pk)
    return jsonify({})


@htmls_api_blueprint.get("/feedbacks")
def retrieve_feedbacks():
    feedbacks = Html \
        .query \
        .filter_by(problem=False) \
        .all()
    return jsonify([feedback.to_dict() for feedback in feedbacks])


@htmls_api_blueprint.post("/feedbacks")
def feedback_html_upload():
    # noinspection DuplicatedCode
    _, html_content, _, prompt, response_a, response_b = parse_bulba_request()

    if not exists(Prompt, prompt=prompt):
        create(Prompt, prompt=prompt)

    prompt_id = Prompt.query.filter_by(prompt=prompt).first().id

    if not exists(Response, response=response_a, prompt_id=prompt_id):
        create(Response, response=response_a, prompt_id=prompt_id)

    if not exists(Response, response=response_b, prompt_id=prompt_id):
        create(Response, response=response_b, prompt_id=prompt_id)

    if exists(Html, content=html_content, problem=False):
        return jsonify({"html": "The feedback already exists."}), 409
    create(Html, problem=False, content=html_content)

    return jsonify({"success": True})


@htmls_api_blueprint.get("/feedbacks/<int:pk>")
def retrieve_feedback(pk: int):
    html = Html.query.get(pk)
    if not html:
        return jsonify({"status": f"Not able to find the Html-{pk}."}), 404
    if html.problem:
        return jsonify({"status": f"The Html-{pk} is not a feedback."}), 404
    return jsonify(html.to_dict())
