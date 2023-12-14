import concurrent
from concurrent.futures import ThreadPoolExecutor

from flask import Blueprint, request, jsonify

from app.utils import parse_html_to_md
from app.utils.v3.oai import *

bulba_v3_api_blueprint = Blueprint('bulba_v3_api', __name__)


@bulba_v3_api_blueprint.post('')
def bulba_v3_determine():
    prompt, response_a, response_b = [
        parse_html_to_md(request.form.get(key))
        for key in ['prompt', 'response_a', 'response_b']
    ]

    with ThreadPoolExecutor() as executor:
        future_to_function = {
            executor.submit(truthful_and_correct, prompt, response_a, response_b): "truthful_and_correct",
            executor.submit(well_written, prompt, response_a, response_b): "truthful_and_correct",
        }

        results = {}
        for future in concurrent.futures.as_completed(future_to_function):
            func_name = future_to_function[future]
            try:
                data = future.result()
                results.update(data)
            except Exception as exc:
                print(f'{func_name} generated an exception: {exc}')

    return jsonify(results)
