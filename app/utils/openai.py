import json

from app.extension import OPENAI_CLIENT


def _chat_complete_json(messages: list):
    res = OPENAI_CLIENT.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=messages,
        response_format={"type": "json_object"},
    )
    result = json.loads(res.choices[0].message.content)
    return result
