from flask import (
    Blueprint,
    jsonify,
)

from app.models import Html, Prompt, Response
from app.utils import parse_bulba_request, clear_scripts
from app.utils.db import *

htmls_api_blueprint = Blueprint('htmls-api', __name__)


@htmls_api_blueprint.get("/problems")
def retrieve_problems():
    problems = Html \
        .query \
        .filter_by(problem=True) \
        .with_entities(Html.task_id) \
        .all()
    return jsonify([task_id for task_id, in problems])


@htmls_api_blueprint.post("/problems")
def problem_html_upload():
    # noinspection DuplicatedCode
    task_id, html_content, _, prompt, response_a, response_b = parse_bulba_request()

    if not exists(Prompt, prompt=prompt):
        create(Prompt, prompt=prompt)

    prompt_id = Prompt.query.filter_by(prompt=prompt).first().id

    if not exists(Response, response=response_a, prompt=prompt_id):
        create(Response, response=response_a, prompt=prompt_id)

    if not exists(Response, response=response_b, prompt=prompt_id):
        create(Response, response=response_b, prompt=prompt_id)

    if exists(Html, task_id=task_id, problem=True):
        return jsonify({"task_id": f"The problem for task-{task_id} already exists."}), 409
    create(Html, task_id=task_id, problem=True, content=html_content)

    return jsonify({"success": True})


@htmls_api_blueprint.get("/problems/<string:task_id>")
def retrieve_problem(task_id: str):
    problem = Html \
        .query \
        .filter_by(task_id=task_id, problem=True) \
        .with_entities(Html.content) \
        .first()
    if not problem:
        return jsonify({"status": f"Not able to find the problem for the task-{task_id}."}), 404
    html_content, = problem
    return Response(clear_scripts(html_content))


@htmls_api_blueprint.delete("/problems/<string:task_id>")
def delete_problem(task_id: str):
    delete(Html, task_id=task_id, problem=True)
    return jsonify({})


@htmls_api_blueprint.get("/feedbacks")
def retrieve_feedbacks():
    problems = Html \
        .query \
        .filter_by(problem=False) \
        .with_entities(Html.task_id) \
        .all()
    return jsonify([task_id for task_id, in problems])


@htmls_api_blueprint.post("/feedbacks")
def feedback_html_upload():
    # noinspection DuplicatedCode
    task_id, html_content, _, prompt, response_a, response_b = parse_bulba_request()

    if not exists(Prompt, prompt=prompt):
        create(Prompt, prompt=prompt)

    prompt_id = Prompt.query.filter_by(prompt=prompt).first().id

    if not exists(Response, response=response_a, prompt=prompt_id):
        create(Response, response=response_a, prompt=prompt_id)

    if not exists(Response, response=response_b, prompt=prompt_id):
        create(Response, response=response_b, prompt=prompt_id)

    if exists(Html, task_id=task_id, problem=False):
        return jsonify({"task_id": f"The feedback for task-{task_id} already exists."}), 409
    create(Html, task_id=task_id, problem=False, content=html_content)

    return jsonify({"success": True})


@htmls_api_blueprint.get("/feedbacks/<string:task_id>")
def retrieve_feedback(task_id: str):
    feedback = Html \
        .query \
        .filter_by(task_id=task_id, problem=False) \
        .with_entities(Html.content) \
        .first()
    if not feedback:
        return jsonify({"status": f"Not able to find the feedback for the task-{task_id}."}), 404
    html_content, = feedback
    return Response(clear_scripts(html_content))
