BASIC_MESSAGES = [
    {"role": "system", "content": "You are a helpful assistant which don't use passive phrases in your whole voice"},
    {"role": "system", "content": "You also rarely use the these vocabularies: tokenizer, dataset, token"},
    {"role": "system", "content": "You also provide some reasons which has at least 17 words"},
    {"role": "system", "content": "We are not interested in your knowledge cutting off. Please don't mention about that"},
]
TRUTHFUL_AND_CORRECT_STATEMENT = """
# Is The Response Truthful And Correct

Identify the correctness of any claims in the explanation and whether the code (if any) is correct and useful. Please take up to 15 minutes to research information across both responses as needed.

Use the following rubric:

| Option        | Reason                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Explanation        |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------|
| No Issues     | All claims in both the explanation and any code comments are factual and accurate; the code (if any) is functional, safe, and useful.                                                                                                                                                                                                                                                                                                                                           | Not Required       |
| Minor Issues  | Either or both of the following are true: <ul><li>Text: primary claims (central to addressing the prompt) are factual/accurate; secondary claims contain meaningful inaccuracies (or unfounded claims). <ul><li>Examples include: an otherwise correct explanation of a library that uses an incorrect link, or a description of a system that misconstrues a small detail of its design.</li></ul></li><li>Code: has minor problems that are straightforward to fix (e.g., missing imports, small syntax errors), or is correct but has misleading comments.</li></ul> | Required if issues are found. Describe all issues. |
| Major Issues  | Either or both of the following are true: <ul><li>Text: primary claims contain meaningful inaccuracies (or unfounded claims), such that the response is not helpful to the user. <ul><li>For example, a response that seriously mischaracterizes the design or usage of a library, or a response that mischaracterizes what the code does.</li></ul></li><li>Code: has one or more of the following problems: <ul><li>Do not use this to flag responses that make simplifying assumptions that a user would reasonably be expected to notice and improve, such as using a hard-coded password in a clearly visible location. </li><li>Functionality: the program does not compile or run and would require substantial effort to repair.</li><li>Safety: the code would create safety or security risks if used, such as relying on libraries with known vulnerabilities or failing to sanitize user inputs.</li><li>Performance: the code is unnecessarily slow, for instance, due to using a quadratic algorithm where a (log-)linear option exists, or repeatedly concatenating long strings instead of using a stringbuilder.</li><li>Documentation: the comments contain meaningful inaccuracies that make the code very hard to understand.</li></ul></li></ul> <br> Important Note: <br> Keep in mind that the code may be functional for the prompter, even if it does not compile or run on your setup. For instance, a response that points to a file only accessible to the prompter, or provides a partial program based on the context provided by the prompter should not be marked as non-functional unless it contains errors that would (likely) manifest in the prompter’s programming context. | Required if issues are found. Describe all issues. |
| Cannot Assess | Cannot determine validity of claims made in the response, or response is a punt ("I am not able to answer that type of question") Select this option if properly researching the claims in the response would take >15 minutes.                                                                                                                                                                                                                                                | Not Required       |
| N/A           | No explicit or implicit claims are made in the response and it does not include code.                                                                                                                                                                                                                                                                                                                                                                                             | Not Required       |
"""
TRUTHFUL_AND_CORRECT_QUESTION = """
I gave you two paragraph (A and B).
Please determine if the paragraphs are truthful and correct.
The output is json format
{
    truthful_and_correct: {
        "A": { // The result for The Response A.
            "type": int // (0 - 4): 0 - "No Issues", 1 - "Minor Issues", 2 - "Major Issues", 3 - "Cannot Assess", 4 - "N/A"
            "reason": ... // Please don't use any type of passive in the sentences. Please describe in 25 - 40 words.
        },
        "B": { // The result for The Response B.
            "type": int, // (0 - 4): 0 - "No Issues", 1 - "Minor Issues", 2 - "Major Issues", 3 - "Cannot Assess", 4 - "N/A"
            "reason": "..." // Please describe in 25 - 40 words. Please don't use any type of passive in the sentences.
        }
    }
}
"""


WELL_WRITTEN_STATEMENT = """
# Is The Response Well Written

Identify whether the answer uses high-quality prose that’s well-organized and easy to read, and whether the included code, if any, is reasonably formatted and includes accurate documentation.

Use the following rubric:

| Option     | Reason                                                                                                                                                               | Explanation            |
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------|
| No Issues  | The response was well-written, coherently organized, and not repetitive. The code, if any, is well-formatted, readable, and reasonably documented.                     | Not required           |
| Minor Issues | Either or both of the following are true: <ul><li>Text: the response had minor issues in writing quality, organization, or repetition, but nothing that really stood out.</li><li>Code: the code (if any) has minor formatting issues or uses overly generic documentation but is otherwise readable.</li></ul> | Required if issues are found. Briefly Describe all issues. |
| Major Issues | Either or both of the following are true: <ul><li>Text: the response was barely intelligible, confusing, or organized poorly enough that it was difficult to read and understand.</li><li>Code: the code (if any) is hard to follow, very poorly formatted, or lacked documentation where it was critically needed.</li></ul> | Required if issues are found. Briefly Describe all issues. |
"""
WELL_WRITTEN_QUESTION = """
I gave you one prompt and two responses (A and B) to the prompt.
Please determine how the responses are well written.
The output is json format
{
    "well_written": {
        "A": { // The result for The Response A.
            "type": int // (0 - 2): 0 - "No Issues", 1 - "Minor Issues", 2 - "Major Issues"
            "reason": ... // Please don't use any type of passive in the sentences. Describe in 25 - 40 words.
        },
        "B": { // The result for The Response B.
            "type": int, // (0 - 2): 0 - "No Issues", 1 - "Minor Issues", 2 - "Major Issues"
            "reason": "..." // Please don't use any type of passive in the sentences. Describe in 25 - 40 words.
        }
    }
}
"""
