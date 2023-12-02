def strip_prompt(prompt: str):
    return prompt.strip()[11:].strip()


def strip_response(response: str):
    return response.strip()[14:].strip()
