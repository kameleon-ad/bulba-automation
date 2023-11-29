from flask import request

from . import parse_html_to_md


def parse_bulba_request(parse_to_markdown=True):
    data_keys = [
        'html_content',
        'instruction',
        'prompt',
        'response_a',
        'response_b',
    ]
    data_list = [request.form.get(data_key) for data_key in data_keys]
    if parse_to_markdown:
        return [parse_html_to_md(data) for data in data_list]
    return data_list
