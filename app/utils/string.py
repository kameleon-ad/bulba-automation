def strip_prompt(prompt: str):
    return prompt.strip()[11:].strip()


def strip_response(response: str):
    return response.strip()[14:].strip()


def normalize_question(question: str):
    return question \
        .replace("Response A", "Response") \
        .replace("Response B", "Response") \
        .replace("response A", "Response") \
        .replace("response B", "Response") \
        .strip() \
        .strip(":") \
        .strip()
