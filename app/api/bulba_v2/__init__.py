import concurrent
from concurrent.futures import ThreadPoolExecutor

from flask import Blueprint, jsonify, request

from app.utils import parse_html_to_md
from app.utils.v2.oai import (
    code_related_and_category_and_complex,
    truthful_and_correct,
    verbose_and_safe_and_harmless,
    overall_quality,
    sxs,
    ftw,
)

bulba_v2_api_blueprint = Blueprint('bulba_v2_api', __name__)


@bulba_v2_api_blueprint.post('')
def bulba_v2_determine():
    prompt, response_a, response_b = [
        parse_html_to_md(request.form.get(key))
        for key in ['prompt', 'response_a', 'response_b']
    ]

    with ThreadPoolExecutor() as executor:
        future_to_function = {
            executor.submit(code_related_and_category_and_complex, prompt): "category",
            executor.submit(truthful_and_correct, prompt, response_a, response_b): "truthful_and_correct",
            executor.submit(sxs, prompt, response_a, response_b): "sxs",
            executor.submit(verbose_and_safe_and_harmless, prompt, response_a, response_b): "verbose_and_safe_and_harmless",
            executor.submit(overall_quality, prompt, response_a, response_b): "overall_quality",
            executor.submit(ftw, prompt, response_a, response_b): "ftw",
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
