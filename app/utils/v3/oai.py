from copy import deepcopy
from typing import Iterable

from app.utils.constants import *
from app.utils.openai import _chat_complete_json


def truthful_and_correct(_prompt: str, response_a: str, response_b: str):
    return _chat_complete_json(_build_truthful_and_correct_messages(_prompt, response_a, response_b))


def well_written(_prompt: str, response_a: str, response_b: str):
    return _chat_complete_json(_build_truthful_and_correct_messages(_prompt, response_a, response_b))


def _build_truthful_and_correct_messages(_prompt: str, response_a: str, response_b: str):
    return __build_messages_with_template_rrsq(
        response_a,
        response_b,
        TRUTHFUL_AND_CORRECT_STATEMENT,
        TRUTHFUL_AND_CORRECT_QUESTION,
    )


def _build_well_written_messages(_prompt: str, response_a: str, response_b: str):
    return __build_messages_with_template_rrsq(
        response_a,
        response_b,
        WELL_WRITTEN_STATEMENT,
        WELL_WRITTEN_QUESTION,
    )


def __build_messages_with_template_rrsq(
    response_a: str,
    response_b: str,
    statement: str,
    question: str,
):
    messages = deepcopy(BASIC_MESSAGES)
    messages.extend([
        {'role': 'user', 'content': 'Here is one response (A).'},
        {'role': 'user', 'content': response_a},
        {'role': 'user', 'content': 'Here is another response (B).'},
        {'role': 'user', 'content': response_b},
        {'role': 'user', 'content': statement},
        {'role': 'user', 'content': question},
    ])
    return messages


def __build_messages_with_template_serrq(
    response_a: str,
    response_b: str,
    examples: Iterable[tuple[str, str]],
    statement: str,
    question: str,
):
    messages = deepcopy(BASIC_MESSAGES)
    messages.append(statement)
    for prompt, ex_response in examples:
        messages.extend([
            {'role': 'user', 'content': prompt},
            {'role': 'user', 'content': question},
            {'role': 'assistant', 'content': ex_response},
        ])
    messages.extend([
        {'role': 'user', 'content': 'Here is one response (A).'},
        {'role': 'user', 'content': response_a},
        {'role': 'user', 'content': 'Here is another response (B).'},
        {'role': 'user', 'content': response_b},
        {'role': 'user', 'content': question},
    ])
    return messages


__all__ = [
    'truthful_and_correct',
    'well_written',
]
