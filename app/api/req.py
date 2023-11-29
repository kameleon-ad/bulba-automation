from flask import Blueprint, request, jsonify

req_api_blueprint = Blueprint('req-api', __name__)


@req_api_blueprint.post("/")
def req_api():
    html_content = request.get_data("html_content")
    with open("4.html", "wb") as fp:
        fp.write(html_content)
    return jsonify({"success": True})
