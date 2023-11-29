from flask import Blueprint, jsonify

from app.models import Html

html_api_blueprint = Blueprint('html-api', __name__)


@html_api_blueprint.get("/problem")
def retrieve_problems():
    problems = Html \
        .query \
        .filter_by(problem=True) \
        .with_entities(Html.task_id) \
        .all()
    return jsonify(problems)


@html_api_blueprint.post("/problem")
def problem_html_upload():
    return jsonify({"success": True})


@html_api_blueprint.post("/feedback")
def feedback_html_upload():
    return jsonify({"success": True})
