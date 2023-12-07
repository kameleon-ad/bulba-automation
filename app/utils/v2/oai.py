import json
from copy import deepcopy

from app.utils.v2.constants import *
from app.extension import OPENAI_CLIENT


def code_related_and_category(prompt: str):
    messages = _build_code_related_and_category_messages(prompt)
    return _chat_complete_json(messages)


def truthful_and_correct(prompt, response_a, response_b):
    messages = _build_truthful_and_correct_messages(prompt, response_a, response_b)
    return _chat_complete_json(messages)


def sxs(prompt, response_a, response_b):
    messages = _build_sxs_messages(prompt, response_a, response_b)
    return _chat_complete_json(messages)


def _chat_complete_json(messages: list):
    res = OPENAI_CLIENT.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=messages,
        response_format={"type": "json_object"},
    )
    result = json.loads(res.choices[0].message.content)
    return result


def _build_code_related_and_category_messages(prompt: str):
    messages = deepcopy(BASIC_MESSAGES)
    messages.extend([
        {"role": "user", "content": CODE_RELATED_STATEMENT},
        {"role": "user", "content": CATEGORY_STATEMENT},
        {"role": "user", "content": RATE_CLARITY_STATEMENT},
        {"role": "user", "content": prompt},
        {"role": "user", "content": CODE_RELATED_AND_CATEGORY_QUESTION}
    ])
    return messages


def _build_truthful_and_correct_messages(prompt: str, response_a: str, response_b: str):
    messages = deepcopy(BASIC_MESSAGES)
    messages.extend([
        {"role": "user", "content": TRUTHFUL_AND_CORRECT_STATEMENT},
        {"role": "user", "content": "Here is the prompt"},
        {"role": "user", "content": prompt},
        {"role": "user", "content": "Here is the Response A"},
        {"role": "user", "content": response_a},
        {"role": "user", "content": "Here is the Response B"},
        {"role": "user", "content": response_b},
        {"role": "user", "content": TRUTHFUL_AND_CORRECT_QUESTION}
    ])
    return messages


def _build_sxs_messages(prompt: str, response_a: str, response_b: str):
    messages = deepcopy(BASIC_MESSAGES)
    messages.extend([
        {"role": "user", "content": SXS_STATEMENT},
        {"role": "user", "content": "Here is the prompt"},
        {"role": "user", "content": prompt},
        {"role": "user", "content": "Here is the response a"},
        {"role": "user", "content": response_a},
        {"role": "user", "content": "Here is the response b"},
        {"role": "user", "content": response_b},
        {"role": "user", "content": "Please generate the answer. And regarding the estimationg of the time. The maximum is 30"},
        {"role": "user", "content": SXS_QUESTION},
    ])
    return messages
