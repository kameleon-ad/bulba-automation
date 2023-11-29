from flask import Blueprint, jsonify

bulba_api_blueprint = Blueprint('bulba-api', __name__)


@bulba_api_blueprint.post("/openai")
def bulba_openai():
    return jsonify({"success": True})
