import json
from copy import deepcopy

from app.utils.v2.constants import BASIC_MESSAGES, CATEGORY_QUESTION, CATEGORY_STATEMENT
from app.extension import OPENAI_CLIENT


def category(prompt: str):
    messages = _build_category_messages(prompt)
    res = OPENAI_CLIENT.chat.completions(
        model="gpt-4-1106-preview",
        messages=messages,
        response_format={"type": "json_object"},
    )
    result = json.loads(res.choices[0].message.content)
    return result["category"]


def _build_category_messages(prompt: str):
    messages = deepcopy(BASIC_MESSAGES)
    messages.extend([
        {"role": "user", "content": BASIC_MESSAGES},
        {"role": "user", "content": CATEGORY_STATEMENT},
        {"role": "user", "content": prompt},
        {"role": "user", "content": CATEGORY_QUESTION}
    ])
    return messages
