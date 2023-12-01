from flask import (
    Blueprint,
    Response,
    jsonify,
)

from app.extension import SQL_DB
from app.models import Html
from app.utils import parse_bulba_request, clear_scripts

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
    task_id, html_content, _, _, _, _ = parse_bulba_request()
    exists = SQL_DB.session.query(
        Html.query.filter_by(task_id=task_id, problem=True).exists()
    ).scalar()
    if exists:
        return jsonify({"task_id": f"The problem for task-{task_id} already exists."}), 409
    Html.create(task_id, True, html_content)
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
    task_id, html_content, _, _, _, _ = parse_bulba_request()
    exists = SQL_DB.session.query(
        Html.query.filter_by(task_id=task_id, problem=False).exists()
    ).scalar()
    if exists:
        return jsonify({"task_id": f"The feedback for task-{task_id} already exists."}), 409
    Html.create(task_id, False, html_content)
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
