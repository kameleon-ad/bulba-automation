from flask import Blueprint, jsonify

from ..models import Answer
from ..utils import parse_bulba_request
from ..utils.openai import DEFAULT_PROMPTS, OPENAI_CLIENT

bulba_api_blueprint = Blueprint('bulba-api', __name__)


@bulba_api_blueprint.post("/openai")
def bulba_openai():
    _, instruction, prompt, response_a, response_b = parse_bulba_request()
    return jsonify({"success": True})


@bulba_api_blueprint.get("/default-prompts")
def bulba_default_prompts():
    res = OPENAI_CLIENT.chat.completions.create(
        model="gpt-4",
        messages=DEFAULT_PROMPTS,
    )
    print(res.choices[0].message.content)
    return jsonify(DEFAULT_PROMPTS)


@bulba_api_blueprint.get("/<int:qid>/<int:pos>")
def bulba_answer(qid: int, pos: int):
    answers = [answer.to_dict() for answer in Answer.query.filter_by(question_id=qid, correct=True).all()]
    if len(answers) == 0:
        return jsonify({"status": "answer not found"}), 404

    question = answers[0]['question']['question']
    instruction = answers[0]['question']['instruction']
    answers = [
        {
            "prompt": answer['response']['prompt']['prompt'],
            "response": answer['response']['response'],
            "answer": answer['answer'],
        } for answer in answers[:-pos]
    ]
    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant",
        },
        {
            "role": "user",
            "content": "Here is one question.",
        },
        {
            "role": "user",
            "content": question,
        },
        {
            "role": "user",
            "content": "Here is the instruction regarding the above question.",
        },
        {
            "role": "user",
            "content": instruction,
        },
        {
            "role": "user",
            "content": "From now, I'll give you one prompt and one response, Please answer about the question I gave "
                       "you. Determine if is there any thing (described in the instruction) in the response.",
        },
    ]
    for answer in answers[:-1]:
        messages.extend([
            {
                "role": "user",
                "content": "Here is the prompt",
            },
            {
                "role": "user",
                "content": answer['prompt'],
            },
            {
                "role": "user",
                "content": "Here is the response",
            },
            {
                "role": "user",
                "content": answer['response'],
            },
            {
                "role": "user",
                "content": "Which type of issues in the above response?",
            },
            {
                "role": "assistant",
                "content": answer['answer'],
            },
        ])
    messages.extend([
        {
            "role": "user",
            "content": "Here is the prompt",
        },
        {
            "role": "user",
            "content": answers[-1]['prompt'],
        },
        {
            "role": "user",
            "content": "Here is the response",
        },
        {
            "role": "user",
            "content": answers[-1]['response'],
        },
        {
            "role": "user",
            "content": "Which type of issues in the above response?",
        },
        {
            "role": "user",
            "content": "And if there is any issues (Major Issues or Minor Issues), please describe the reason why in "
                       "15 ~ 40 words?"
        }
    ])
    res = OPENAI_CLIENT.chat.completions.create(
        model="gpt-4",
        messages=messages,
    )
    rlt = {
        "gpt": res.choices[0].message.content,
        "correct": answers[-1]['answer'],
        "prompt": answers[-1]['prompt'],
        "response": answers[-1]['response'],
        "question": question,
    }
    print(res.choices[0].message.content)
    print(answers[-1]['answer'])
    return jsonify(rlt)
