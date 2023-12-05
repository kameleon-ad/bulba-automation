from flask import Blueprint, jsonify, request
from copy import deepcopy

from app.models import Sample, Question
from app.utils.db import *
from oai import OPENAI_CLIENT
from oai.constants import BASE_PROMPTS, BASE_STATEMENT

samples_api_blueprint = Blueprint('samples', __name__)


@samples_api_blueprint.get('')
def retrieve_samples():
    samples = [sample.to_dict() for sample in Sample.query.all()]
    return jsonify(samples)


@samples_api_blueprint.post('')
def create_sample():
    prompt = request.form.get('prompt')
    response = request.form.get('response')
    question_id = request.form.get('question_id')
    reason = request.form.get('reason')
    answer = request.form.get('answer')
    return jsonify(get_create(
        Sample,
        prompt=prompt,
        response=response,
        question_id=question_id,
        reason=reason,
        answer=answer
    ).to_dict())


@samples_api_blueprint.get('/<int:qid>')
def ask_question(qid: int):
    samples = Sample.query.all()
    messages = deepcopy(BASE_PROMPTS)
    target_question = Question.query.get(qid)
    for qid in range(26, 29):
        question = Question.query.get(qid)
        messages.extend([
            {"role": "user", "content": "Here is one question"},
            {"role": "user", "content": question.question},
            {"role": "user", "content": "Here is the instruction for the above question"},
            {"role": "user", "content": question.instruction},
            {"role": "user", "content": BASE_STATEMENT},
        ])
    prompt = request.form.get('prompt')
    response = request.form.get('response')
    for sample in samples:
        messages.extend([
            {"role": "user", "content": "Here is the prompt."},
            {"role": "user", "content": sample.prompt},
            {"role": "user", "content": "Here is the response."},
            {"role": "user", "content": sample.response},
            {"role": "user", "content": f"Evaluate the response to the prompt, the question is {sample.question.question}"},
            {"role": "assistant", "content": sample.reason},
            {"role": "user", "content": f"So, what kind of issues are in the response?"},
            {"role": "assistant", "content": sample.answer},
        ])
    messages.extend([
            {"role": "user", "content": "Here is the prompt."},
            {"role": "user", "content": prompt},
            {"role": "user", "content": "Here is the response."},
            {"role": "user", "content": response},
            {"role": "user", "content": f"Evaluate the response to the prompt, the question is {target_question.question} in "
                                        f"15 ~ 40 words. And what kind of issues are in the response?"},
    ])
    res = OPENAI_CLIENT.chat.completions.create(
        model="gpt-4",
        messages=messages,
    )
    rlt = {
        "gpt": res.choices[0].message.content,
        "prompt": prompt,
        "response": response,
        "question": target_question.question,
    }
    return jsonify(rlt)