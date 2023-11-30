from flask import request

from . import parse_html_to_md


def parse_bulba_request(parse_to_markdown=True):
    data_keys = [
        'task_id',
        'html_content',
        'instruction',
        'prompt',
        'response_a',
        'response_b',
    ]
    parsed_data = {data_key: request.form.get(data_key) for data_key in data_keys}

    if parse_to_markdown:
        for data_key in data_keys[-4:]:
            parsed_data[data_key] = parse_html_to_md(parsed_data[data_key])

    return map(lambda data_key: parsed_data[data_key], data_keys)
