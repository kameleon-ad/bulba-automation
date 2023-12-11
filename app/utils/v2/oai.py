import json
from copy import deepcopy

from app.utils.v2.constants import *
from app.extension import OPENAI_CLIENT


def code_related_and_category_and_complex(prompt: str):
    messages = _build_code_related_and_category_and_complex_messages(prompt)
    return _chat_complete_json(messages)


def truthful_and_correct(prompt, response_a, response_b):
    messages = _build_truthful_and_correct_messages(prompt, response_a, response_b)
    return _chat_complete_json(messages)


def ftw(prompt: str, response_a: str, response_b: str):
    return _chat_complete_json(_build_ftw_messages(prompt, response_a, response_b))


def verbose_and_safe_and_harmless(prompt, response_a, response_b):
    messages = _build_verbose_and_safe_and_harmless_messages(prompt, response_a, response_b)
    return _chat_complete_json(messages)


def overall_quality(prompt, response_a, response_b):
    messages = _build_overall_quality(prompt, response_a, response_b)
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


def _build_ftw_messages(prompt: str, response_a: str, response_b: str):
    return __build_messages_with_template_ssqrrp(
        prompt,
        response_a,
        response_b,
        (
            FOLLOW_INSTRUCTION_STATEMENT,
            TRUTHFUL_AND_CORRECT_STATEMENT,
            WELL_WRITTEN_STATEMENT,
        ),
        FTW_QUESTION,
    )


def _build_code_related_and_category_and_complex_messages(prompt: str):
    messages = deepcopy(BASIC_MESSAGES)
    messages.extend([
        {"role": "user", "content": CODE_RELATED_STATEMENT},
        {"role": "user", "content": CATEGORY_STATEMENT},
        {"role": "user", "content": RATE_CLARITY_STATEMENT},
        {"role": "user", "content": COMPLEXITY_QUESTION},
        {"role": "user", "content": "Here is the prompt"},
        {"role": "user", "content": prompt},
        {"role": "user", "content": CODE_RELATED_AND_CATEGORY_AND_COMPLEXITY_QUESTION}
    ])
    return messages


def _build_truthful_and_correct_messages(prompt: str, response_a: str, response_b: str):
    return __build_messages_with_template_sprrq(
        prompt,
        response_a,
        response_b,
        TRUTHFUL_AND_CORRECT_STATEMENT,
        TRUTHFUL_AND_CORRECT_QUESTION,
    )


def _build_verbose_and_safe_and_harmless_messages(prompt: str, response_a: str, response_b: str):
    messages = deepcopy(BASIC_MESSAGES)
    messages.extend([
        {"role": "user", "content": HOW_VERBOSE_STATEMENT},
        {"role": "user", "content": HARMLESS_STATEMENT},
        {"role": "user", "content": "Here is the prompt"},
        {"role": "user", "content": prompt},
        {"role": "user", "content": "Here is the response a"},
        {"role": "user", "content": response_a},
        {"role": "user", "content": "Here is the response b"},
        {"role": "user", "content": response_b},
        {"role": "user", "content": VERBOSE_HARMLESS_QUESTION},
    ])
    return messages


def _build_overall_quality(prompt: str, response_a: str, response_b: str):
    return __build_messages_with_template_sprrq(
        prompt,
        response_a,
        response_b,
        OVERALL_RATING_STATEMENT,
        OVERALL_RATING_QUESTION,
    )


def _build_sxs_messages(prompt: str, response_a: str, response_b: str):
    return __build_messages_with_template_sprrq(
        prompt,
        response_a,
        response_b,
        SXS_STATEMENT,
        SXS_QUESTION,
    )


def __build_messages_with_template_sprrq(prompt: str, response_a: str, response_b: str, statement: str, question: str):
    messages = deepcopy(BASIC_MESSAGES)
    messages.extend([
        {"role": "user", "content": statement},
        {"role": "user", "content": "Here is the prompt"},
        {"role": "user", "content": prompt},
        {"role": "user", "content": "Here is the response a"},
        {"role": "user", "content": response_a},
        {"role": "user", "content": "Here is the response b"},
        {"role": "user", "content": response_b},
        {"role": "user", "content": question},
    ])
    return messages


def __build_messages_with_template_ssqrrp(
    prompt: str,
    response_a: str,
    response_b: str,
    statements: iter[str],
    question: str,
):
    messages = deepcopy(BASIC_MESSAGES)
    messages.extend(({"role": "user", "content": statement} for statement in statements))
    messages.extend([
        {"role": "user", "content": "Here is the prompt"},
        {"role": "user", "content": prompt},
        {"role": "user", "content": "Here is the response a"},
        {"role": "user", "content": response_a},
        {"role": "user", "content": "Here is the response b"},
        {"role": "user", "content": response_b},
        {"role": "user", "content": question},
    ])
    return messages
