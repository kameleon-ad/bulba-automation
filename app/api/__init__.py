from flask import Blueprint, jsonify, request

# from .req import req_api_blueprint

api_blueprint = Blueprint('api', __name__)
# api_blueprint.register(req_api_blueprint, url_prefix='/req')


@api_blueprint.get('/health')
def api_health():
    return jsonify({"status": "UP"})


@api_blueprint.post("/")
def req_api():
    html_content = request.form.get("html_content")
    with open("4.html", "wb") as fp:
        fp.write(html_content.encode(errors="ignore"))
    return jsonify({"success": True})
