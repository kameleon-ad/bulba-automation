TRUTHFUL_AND_CORRECT_QUESTION_EXAMPLE = """
I gave you one paragraph (A and B).
Please determine if the paragraph is truthful and correct.
The output is json format
{
    truthful_and_correct: {
        "type": int // (0 - 4): 0 - "No Issues", 1 - "Minor Issues", 2 - "Major Issues", 3 - "Cannot Assess", 4 - "N/A"
        "reason": ... // If the type is (0) No Issues, in that case, there is no need to use "reason" field. Also "B" is same with this. Please don't use any type of passive in the sentences. If the type is not Just Right, in that case please describe in 25 - 40 words. Please don't use any type of passive in the sentences.
    }
}
"""
