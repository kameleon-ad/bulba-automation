from flask import Blueprint, jsonify, request

bulba_v2_api_blueprint = Blueprint('bulba_v2_api', __name__)


@bulba_v2_api_blueprint.post('')
def bulba_v2_determine():
    return jsonify(request.form.keys())
