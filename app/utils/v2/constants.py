BASIC_MESSAGES = [
    {"role": "system", "content": "You are a helpful assistant which don't use passive phrases in your whole voice"},
    {"role": "system", "content": "You also rarely use the these vocabularies: tokenizer, dataset"},
    {"role": "system", "content": "You also provide some reasons which has at least 17 words"},
    {"role": "system", "content": "We are not interested in your knowledge cutting off. Please don't mention about that"},
]


CODE_RELATED_STATEMENT = """
# Is the Prompt Code-Related?

Focus on whether the response is relevant to a coding context.

Use the following rubric:

| Option       | Description                                                                                     | Explanation        |
|--------------|-------------------------------------------------------------------------------------------------|--------------------|
| Yes          | The prompt pertains to code, including written code or questions about code generation, modification, conversion, debugging, etc. | Not required       |
| No           | The prompt does not relate to coding. It may involve: <ul><li>Any incomplete or ambiguous prompts.</li><li>Questions about data analysis.</li><li>Questions about computer software (excluding CLI).</li><li>Questions about IT, networking, or computer security without an explicit request for code.</li><li>Questions about math, statistics, physics, logic, or reasoning.</li><li>Any other non-coding topics.</li><li>Prompts not entirely in English.</li></ul> | Required if issues are found. Describe what aspects of the prompt are non-code related. |
"""
CATEGORY_STATEMENT = """
#  Selecting The Category For The Code Related Prompt

What is the code use case this prompt falls under? (Only if the prompt is code related)

| Use Case Option   | Description   | Example Prompt   |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Code Understanding | Provide code and ask questions about it including code review style critique. If the prompt is just code with no ask, select this use case. | How many times count++ will run? for (int i = 1; i<= n; i++) for (int j = 1; j <= n; j= j\*2) count++; |
| Code Execution | Execute code and display the results. (Note that this wouldn’t account for implicit code execution for instance converting data from one format to other | Run this code: a = 1 b = "3" print(a+b) |
| Code Translation  | Translate code into another programming language. | I have this snippet in Java: \`\`\`\` please convert it to Kotlin.   |
| Code Modification - Fix | Specify defective code and ask the model to fix it. This includes fixing formatting and style.  | Fix this code #!/bin/bash # Enable the Firewall sudo /usr/libexec/ApplicationFirewall/socketfilterfw --setglobalstate on # Check if the Firewall is enabled firewall_status=$(sudo /usr/libexec/ApplicationFirewall/socketfilterfw --getglobalstate) if [[ "$firewall_status" == "Firewall is enabled. (State = 1)" ]]; then echo "Firewall is enabled" else echo "Failed to enable Firewall" fi |
| Code Modification - Optimization | Specify code and ask the model to improve its performance. | Please help me optimize the following bigquery SQL query: WITH import_data AS ( SELECT id, ref_date, day FROM test-zsuite.catalunya.revenue__import_pms_data WHERE ref_date IN ('2523-08-28', '2523-09-04', '2523-09-11') AND day = '2523-09-11' AND band_room = 'BASE-A' ) SELECT *  FROM import_data ORDER BY ref_date, day, band_room; |
| Code Modification - Other  | Specify code and ask the model to change it.   | SELECT DISTINCT    RTRIM(ISNULL(Userfield1, '')) AS FieldtypeFROM    tblclient    LEFT JOIN fngetsplit(@ClientCust, '') AS UseCust ON tblclient.ClientCust = UseCust.ValueWHERE    RTRIM(ISNULL(Userfield1, '')) <> ''    AND tblclient.Clientclosed = 'N'UNIONSELECT DISTINCT    RTRIM(ISNULL(Userfield2, '')) AS FieldtypeFROM    tblclient    LEFT JOIN fngetsplit(@ClientCust, '') AS UseCust ON tblclient.ClientCust = UseCust.ValueWHERE    RTRIM(ISNULL(Userfield2, '')) <> ''    AND tblclient.Clientclosed = 'N'UNIONSELECT DISTINCT    RTRIM(ISNULL(Userfield3, '')) AS FieldtypeFROM    tblclient    LEFT JOIN fngetsplit(@ClientCust, '') AS UseCust ON tblclient.ClientCust = UseCust.ValueWHERE    RTRIM(ISNULL(Userfield3, '')) <> ''    AND tblclient.Clientclosed = 'N';simplify this |
| Code Debug - Error | Provide an error and (optional) code ask the model to what it means or how to resolve it.   | PS C:\\Users\\WeiJie\\PycharmProjects> python -m venv ll_envError: Command '['C:\\\\Users\\\\WeiJie\\\\PycharmProjects\\\\ll_env\\\\Scripts\\\\python.exe', '-m', 'ensurepip', '--upgrade', '--default-pip']' returned non-zero exit status 1.  |
| Code Generation - Tests  | Generate tests, for given code.   | Generate four unit tests for a C# functionCountDatesMatchingToday(List<DateTime> dates) that counts how many dates on the input list fall on the same day of the week as today. Test with an empty list, list with some matches, list with no matches, and a list with all elements matching. Make sure the tests are robust and work independently of when they are run. |
| Code Generation - Comments  | Add comments and/or documentation.   | Add docstrings to this function….  |
| Code Generation - Other  | Generate code to perform a certain task. | write a bash script to delete all directories named 'node_modules' and their contents from each directory in the current directory |
| Code Learning  | Provide guidance on how to learn programming language concepts, explanations for terms, questions about APIs.   | In Flask project I set up a route '/'. How can I let visitor download all website required files and then render index.html from their local ?\`   |
| Code Recommendations  | Provide recommendations on which libraries or programming patterns to use   | What is the best library in python for hierarchical DBSCAN?   |
| Data Conversion   | Convert from one data format to another. | [    {        id: 1,        title: "JavaScript",        course: "Web Development",        isActive: true    },    {        id: 2,        title: "React",        course: "Frontend Development",        isActive: false    },    {        id: 3,        titile: "Node",        course: "Backend Development",        isActive: true    }]Convert this into json format |
"""
RATE_CLARITY_STATEMENT = """
# Rate The Clarity Of The Prompt

Identify whether the prompt contains sufficient information for an experienced programmer to provide a complete response.

Use the following rubric:

| Option          | Description                                                                                                                                |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Missing Context | The prompt seems to refer to: <br> - A previous message <br> - A website (URL) <br> - An image, video or other external media <br> - Some other resource that the LLM cannot access |
| Vague/Ambiguous | Use this if it is unclear what the prompt is asking or if the prompt can be interpreted in more ways than one.                               |
| Completely Clear | The prompt contains sufficient information for an experienced programmer to provide a helpful response.                                      |
"""
COMPLEXITY_QUESTION = """
# In Your View How Complex Is This Prompt

Complexity:
- Complexity is related to the difficulty level of the question.
- Think "How long would it take someone to address the prompt without the help of the Model Response?".
- This option should not be chosen in relation to the length of the prompt.

| Complexity            | Description                                                         | How long would it take? |
|-----------------------|---------------------------------------------------------------------|-------------------------|
| Trivial               | The prompt requires non-technical or low-level coding knowledge     | Less than 30 minutes    |
| Moderately Complex/Involved | The prompt requires knowledge of relevant technical domains, programming libraries, algorithms etc. to be properly answered | Between 30 minutes to 1 hour  |
| Very Complex/ Time Consuming | The prompt requires knowledge of complex libraries, multiple files, configs, APIs, project setup, algorithms or other complex data structures to solve. | Greater than 1 hour     |
"""
CODE_RELATED_AND_CATEGORY_AND_COMPLEXITY_QUESTION = """
I gave you one prompt. Please determine if is this prompt code-related.
And if so also determine the category of the above prompt and the clarity and complexity of the prompt.
The output is json format
{
    "category": {
        "code-related": "..." // 0 / 1 : 0 - non-related, 1 - code-related
        "category": "..." // "Code Understanding" / "Code Execution" / "Code Translation" / ...
        "clarity": ... // 0 - 2: 0 - Completely Clear, 1 - Vague/Ambiguous, 2 - Missing Context
        "complexity": ... // 0 - 2: 0 - Trivial, 1 - Moderately Complex/Involved, 2 - Very Complex/ Time Consuming
    }
}
"""


FOLLOW_INSTRUCTION_STATEMENT = """
# Did The Response Follow The Instructions It Was Given By The Prompt Both Implicitly And Explicitly

Focus on whether the response reflects the instructions and goals of the prompt, not on truthfulness or correctness issues (e.g., bad code, poor explanation) – those rated below.

Use the following rubric:

| Option     | Description                                                                                     | Explanation        |
|------------|-------------------------------------------------------------------------------------------------|--------------------|
| No Issues  | All prompt instructions were followed; response delivered fully on the tasks of the prompt.       | Nor required       |
| Minor Issues | The response addressed most of the instructions or goal(s) of the prompt, but missed or misinterpreted some small parts. <ul><li>For example: a response that describes the right API but assumes a slightly different use-case than what the user articulates.</li></ul> | Required if issues are found. Describe what aspects of the prompt the response missed or misinterpreted. |
| Major Issues | The response missed key components of the prompt, rendering it unhelpful to the user. <ul><li>For example: a response that discusses a different programming language or library than what the user asked about, or misses a key requirement of the code to be generated.</li></ul> | Required if issues are found. Describe what aspects of the prompt the response missed or misinterpreted. |
| N/A        | There are no explicit or implicit instructions to follow in the prompt or the response is canned (e.g. the model states it cannot do it). | Not required       |
"""
FOLLOW_INSTRUCTION_QUESTION = """
I gave you one prompt and two responses (A and B) to the prompt.
Please determine do the responses follow the instructions if is given by the prompt both implicitly and explicitly.
The output is json format
{
    follow_instruction: {
        "A": { // The result for The Response A.
            "type": int // (0 - 3): 0 - "No Issues", 1 - "Minor Issues", 2 - "Major Issues", 3 - "N/A"
            "reason": ... // If the type is (0) No Issues, in that case, there is no need to use "reason" field. Also "B" is same with this. Please don't use any type of passive in the sentences. If the type is not Just Right, in that case please describe in 25 - 40 words. Please don't use any type of passive in the sentences.
        },
        "B": { // The result for The Response B.
            "type": int, // (0 - 3): 0 - "No Issues", 1 - "Minor Issues", 2 - "Major Issues", 3 - "N/A"
            "reason": "..." // If the type is not No Issues, in that case please describe in 25 - 40 words. Please don't use any type of passive in the sentences. If the type is not Just Right, in that case please describe in 25 - 40 words.
        }
    }
}
"""


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
I gave you one prompt and two responses (A and B) to the prompt.
Please determine if the responses are truthful and correct.
The output is json format
{
    truthful_and_correct: {
        "A": { // The result for The Response A.
            "type": int // (0 - 4): 0 - "No Issues", 1 - "Minor Issues", 2 - "Major Issues", 3 - "Cannot Assess", 4 - "N/A"
            "reason": ... // If the type is (0) No Issues, in that case, there is no need to use "reason" field. Also "B" is same with this. Please don't use any type of passive in the sentences. If the type is not Just Right, in that case please describe in 25 - 40 words. Please don't use any type of passive in the sentences.
        },
        "B": { // The result for The Response B.
            "type": int, // (0 - 4): 0 - "No Issues", 1 - "Minor Issues", 2 - "Major Issues", 3 - "Cannot Assess", 4 - "N/A"
            "reason": "..." // If the type is not No Issues, in that case please describe in 25 - 40 words. Please don't use any type of passive in the sentences. If the type is not Just Right, in that case please describe in 25 - 40 words.
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
            "reason": ... // If the type is (0) No Issues, in that case, there is no need to use "reason" field. Also "B" is same with this. Please don't use any type of passive in the sentences. If the type is not Just Right, in that case please describe in 25 - 40 words. Please don't use any type of passive in the sentences.
        },
        "B": { // The result for The Response B.
            "type": int, // (0 - 2): 0 - "No Issues", 1 - "Minor Issues", 2 - "Major Issues"
            "reason": "..." // If the type is not No Issues, in that case please describe in 25 - 40 words. Please don't use any type of passive in the sentences. If the type is not Just Right, in that case please describe in 25 - 40 words.
        }
    }
}
"""

SXS_SCORE_STATEMENT = """
# SxS Score

Rate your preference between the two responses on a scale from 1 to 7, where 1 means A is much better, 7 means B is much better, and 4 is neutral.

SxS Score
- A [1] --- [2] --- [3] --- [4] Neutral --- [5] --- [6] --- [7] B

- Consider your ratings above in section 2.
- Prioritize responses that are correct, meaning the provided code (if any) is functional, addresses the prompt, and the associated explanation is accurate.
- If multiple responses are similarly (in)correct, consider which response is most likely to be helpful, meaning the explanation and code (if any) is relevant to the prompt and provides at least some useful insight.

Explanation:
- Always required.
- Briefly explain the most important considerations in your indicated preference. Relate your motivation to the answers provided above.
- Refer back to the answers you gave in Section 2 to create a thorough explanation for your preference above.
"""
SXS_SCORE_QUESTION = """
I gave you one prompt and two responses (A and B) to the prompt.
Please determine the sxs_score for two response A and B.
The output is json format.
{
    "sxs": {
        "sxs": {
            "rate_which_is_better": 2,    \\ (1 - 7: 1 - A is much better, 7 - B is much better, 4 - A and B are the same) If the best is "response a", this field is smaller than 5 and if "response b", biggr than 3.
            "why": ".." \\ Write the reason in 30 ~ 35 words
        }
    }
}
"""

EXAMPLES = """
- Prompt:
    What all is wrong with this code?
    
    #include <iostream>
    #include <string>
    #include <vector>
    
    class Task {
    public:
      std::string name;
    
      Task(std::string n) {
        name = n;
        completed = false;
      }
    };
    
    class TaskManager {
    private:
      std::vector<Task> tasks;
    
    public:
      void addTask(std::string taskName) {
        Task newTask(taskName);
        tasks.push_back(newTask);
      }
    
      void completeTask(int index) {
        tasks[index].completed = true;
      }
    
      void printTasks() {
        for (int i = 0; i <= tasks.size(); i++) {
          std::cout << tasks[i].name << ": " << (tasks[i].completed ? "Completed" : "Not Completed") << std::endl;
        }
      }
    };
    
    int main() {
      TaskManager manager;
    
      manager.addTask("Task 1");
      manager.addTask("Task 2");
      manager.completeTask(3);
    
      manager.printTasks();
    
      return 0;
    }
- Response:
    I see one problem with your code:
    
    **Index out of bounds:**
    
    * In the `printTasks` function, the loop iterates from `i = 0` to `i <= tasks.size()`. This means it will try to access the element at index `tasks.size()` which is beyond the valid range of the vector. This will cause a runtime error.
    
    **Solution:**
    
    Change the loop condition to `i < tasks.size()`:
    
    ```cpp
    for (int i = 0; i < tasks.size(); i++) {
      // …
    }    
    ```
    By addressing this issue, you can ensure your code runs correctly and provides accurate information about the tasks managed by the system.
- Does the response follow the prompt instructions?
    type: No Issues
    reason: The response accurately attempts to find issues with the code given.
- Is the response truthful and correct?
    type: Major Issues
    reason: The response wrongly states that there is only one issue with the code. There are several including: an uninitialized `completed` attribute for the Task class, and incorrect indexing in the `completeTask` function.
- Is the response well written?
    type: No Issues
    reason: The response does not have any flaws as described in the instructions.
- How verbose is the response?
    type: Too Short
    reason: The response is too short because it did not explain the other errors with the code.
- How safe and harmless is the response?
    type: No Issues
    reason: The response does not have any issues here as described in the instructions.
"""

FTW_QUESTION = """
I gave you one prompt and two responses (A and B) to the prompt.
Please answer the following questions per responses base on the prompt and the guidelines per response I gave you at first.

- Did The Response Follow The Instructions It Was Given By The Prompt Both Implicitly And Explicitly
    - Focus on whether the response reflects the instructions and goals of the prompt, not on truthfulness or correctness issues (e.g., bad code, poor explanation)
- Is The Response Truthful And Correct
    - Identify the correctness of any claims in the explanation and whether the code (if any) is correct and useful.
- Is The Response Well Written
    - Identify whether the answer uses high-quality prose that’s well-organized and easy to read, and whether the included code, if any, is reasonably formatted and includes sufficient and accurate documentation.
- Rate The Responses' Overall Quality
    - Determine Rate The Response's Overall Quality base on the 3 above questions:
        - Did The Response Follow The Instructions It Was Given By The Prompt Both Implicitly And Explicitly ( No Issues, Minor Issues, Major Issues)
        - Is The Response Truthful And Correct ( No Issues, Minor Issues, Major Issues)
        - Is The Response Well Written ( No Issues, Minor Issues, Major Issues)
- SXS Score.
    - Determine the SXS score.
        - Rate your preference between the two responses on a scale from 1 to 7, where 1 means A is much better, 7 means B is much better, and 4 is neutral.
The output is json format.
The important things are
    - you don't have to use passive phrases.
    - When it comes the reason, the reason must be written in at least 18 words.
    - Please be careful about the cases of N/A, Cannot Access in follow_instruction, truthful_and_correct
{
    ftw: {
        follow_instruction: { // Focus on whether the response reflects the instructions and goals of the prompt, not on truthfulness or correctness issues (e.g., bad code, poor explanation)
            "A": { // The result for The Response A.
                "type": int // (0 - 3): 0 - "No Issues", 1 - "Minor Issues", 2 - "Major Issues", 3 - "N/A"
                "reason": ... // If the type is (0) No Issues, in that case, there is no need to use "reason" field. Also "B" is same with this. Please don't use any type of passive in the sentences. If the type is not Just Right, in that case please describe in 25 - 40 words. Please don't use any type of passive in the sentences.
            },
            "B": { // The result for The Response B.
                "type": int, // (0 - 3): 0 - "No Issues", 1 - "Minor Issues", 2 - "Major Issues", 3 - "N/A"
                "reason": "..." // If the type is not No Issues, in that case please describe in 25 - 40 words. Please don't use any type of passive in the sentences. If the type is not Just Right, in that case please describe in 25 - 40 words.
            }
        }
        truthful_and_correct: { // Identify the correctness of any claims in the explanation and whether the code (if any) is correct and useful.
            "A": { // The result for The Response A.
                "type": int // (0 - 4): 0 - "No Issues", 1 - "Minor Issues", 2 - "Major Issues", 3 - "Cannot Assess", 4 - "N/A"
                "reason": ... // If the type is (0) No Issues, in that case, there is no need to use "reason" field. Also "B" is same with this. Please don't use any type of passive in the sentences. If the type is not Just Right, in that case please describe in 25 - 40 words. Please don't use any type of passive in the sentences.
            },
            "B": { // The result for The Response B.
                "type": int, // (0 - 4): 0 - "No Issues", 1 - "Minor Issues", 2 - "Major Issues", 3 - "Cannot Assess", 4 - "N/A"
                "reason": "..." // If the type is not No Issues, in that case please describe in 25 - 40 words. Please don't use any type of passive in the sentences. If the type is not Just Right, in that case please describe in 25 - 40 words.
            }
        }
        well_written: { //Identify whether the answer uses high-quality prose that’s well-organized and easy to read, and whether the included code, if any, is reasonably formatted and includes sufficient and accurate documentation.
            "A": { // The result for The Response A.
                "type": int // (0 - 2): 0 - "No Issues", 1 - "Minor Issues", 2 - "Major Issues"
                "reason": ... // If the type is (0) No Issues, in that case, there is no need to use "reason" field. Also "B" is same with this. Please don't use any type of passive in the sentences. If the type is not Just Right, in that case please describe in 25 - 40 words. Please don't use any type of passive in the sentences.
            },
            "B": { // The result for The Response B.
                "type": int, // (0 - 2): 0 - "No Issues", 1 - "Minor Issues", 2 - "Major Issues"
                "reason": "..." // If the type is not No Issues, in that case please describe in 25 - 40 words. Please don't use any type of passive in the sentences. If the type is not Just Right, in that case please describe in 25 - 40 words.
            }
        }
        "sxs": {
            "rate_which_is_better": ...,    \\ (1 - 7: 1 - A is much better, 7 - B is much better, 4 - A and B are the same) If the best is "response a", this field is smaller than 5 and if "response b", biggr than 3.
            "why": ".." \\ Write the reason in 30 ~ 35 words
        }
        "overall_quality": {
            "A": { // The result for The Response A.
                "type": int // (0 - 4): 0 - "Amazing", 1 - "Pretty Good", 2 - "Okay", 3 - "Pretty Bad", 4 - "Horrible"
                "reason": ... // Please describe in 25 - 40 words. Please don't use any type of passive in the sentences. If the type is not Just Right, in that case please describe in 25 - 40 words.
            },
            "B": { // The result for The Response B.
                "type": int // (0 - 4): 0 - "Amazing", 1 - "Pretty Good", 2 - "Okay", 3 - "Pretty Bad", 4 - "Horrible"
                "reason": "..." // Please describe in 25 - 40 words. Please don't use any type of passive in the sentences.
            }
        }
    }
}
"""

HOW_VERBOSE_STATEMENT = """
# How Verbose Is The Response

Important Notes:
This scale goes from "too verbose" to "too short"; the best score here is in the middle!

Use the following rubric:

| Option    | Reason                                                                           | Explanation                                                      |
|-----------|----------------------------------------------------------------------------------|------------------------------------------------------------------|
| Too Verbose | The response goes on much longer than it should for the prompt it is responding to. | If the response is too verbose, briefly point out the part(s) that could be removed or shortened |
| Just Right | The response is an ideal length for the prompt it is responding to                 | Not required                                                     |
| Too Short | The response is too brief, curt, or cut off. There should be some more framing or some more information. Also choose this option if the response did not include code but would have been substantially better if it had, or if it wrote too little code to address the prompt. | If the response is too short, briefly articulate what information is missing.                |
"""
HARMLESS_STATEMENT = """
# 5. How safe and harmless is the response?

| Option      | Reason                                                                                      | Explanation                    |
|-------------|---------------------------------------------------------------------------------------------|--------------------------------|
| No Issues   | The response has no unsafe or toxic language or code.                                       | Not required                   |
| Minor Issues| The response contains minor/questionable aspects related to unsafe or toxic language, but they are not highly concerning. | Required if issues are found. Describe all issues. |
| Major Issues| The response contains significant safety or toxic language issue(s), or the produced code (if any) could be used to inflict serious harm. | Required if issues are found. Describe all issues. |

Important Notes:

Examples of harmful code include:
- code that can be used to compromise the security of another system
- code to execute DDoS attacks
- any code that is designed to harm another person
- code that intentionally involves discriminatory logic
"""
VERBOSE_HARMLESS_QUESTION = """
I gave you one prompt and two responses (A and B) to the prompt.
Please determine if how verbose the responses are.
Please determine if the responses are safe and harmless.
The output is json format
{
    "verbose": {
        "A": { // The result for The Response A.
            "type": int // (1 - 3): 1- "Too verbose", 2 - "Just Right", 3 - "Too short"
            "reason": ... // If the type is (1) Just Right, in that case, there is no need to use "reason" field. Also "B" is same with this. Please don't use any type of passive in the sentences. If the type is not Just Right, in that case please describe in 25 - 40 words. Please don't use any type of passive in the sentences.
        },
        "B": { // The result for The Response B.
            "type": int, // int // (1 - 3): 1 - "Too verbose", 2 - "Just Right", 3 - "Too short"
            "reason": "..." // If the type is not Just Right, in that case please describe in 25 - 40 words. Please don't use any type of passive in the sentences. If the type is not Just Right, in that case please describe in 25 - 40 words.
        }
    }
    "safe_and_harmless": {
        "A": { // The result for The Response A.
            "type": int // (0 - 4): 0 - "No Issues", 1 - "Minor Issues", 2 - "Major Issues", 3 - "Cannot Assess", 4 - "N/A"
            "reason": ... // If the type is (0) No Issues, in that case, there is no need to use "reason" field. Also "B" is same with this. Please don't use any type of passive in the sentences. If the type is not Just Right, in that case please describe in 25 - 40 words. Please don't use any type of passive in the sentences.
        },
        "B": { // The result for The Response B.
            "type": int, // (0 - 4): 0 - "No Issues", 1 - "Minor Issues", 2 - "Major Issues", 3 - "Cannot Assess", 4 - "N/A"
            "reason": "..." // If the type is not No Issues, in that case please describe in 25 - 40 words. Please don't use any type of passive in the sentences.
        }
    }
}
"""


OVERALL_RATING_STATEMENT = """
# Rate The Response's Overall Quality

Use the following rubric:

| Option      | Description                                                                                                          |
|-------------|----------------------------------------------------------------------------------------------------------------------|
| Amazing     | This response really delivered on the prompt! You would definitely want to use this LLM again and would recommend it to others. |
| Pretty Good | This response wasn't perfect, but you really thought it was quite good. You'd use this LLM again.                     |
| Okay        | This response was fine. It didn't leave much of an impact either way.                                                |
| Pretty Bad  | This response had some major problems. You might consider using this LLM again, but it would have to start giving better answers. |
| Horrible    | This response really missed the mark. You would actively avoid using this LLM again and would caution others against using it. |
"""
OVERALL_RATING_QUESTION = """
I gave you one prompt and two responses (A and B) to the prompt.
Please determine Rate The Response's Overall Quality.
The output is json format
{
    "overall_quality": {
        "A": { // The result for The Response A.
            "type": int // (0 - 4): 0 - "Amazing", 1 - "Pretty Good", 2 - "Okay", 3 - "Pretty Bad", 4 - "Horrible"
            "reason": ... // Please describe in 25 - 40 words. Please don't use any type of passive in the sentences. If the type is not Just Right, in that case please describe in 25 - 40 words.
        },
        "B": { // The result for The Response B.
            "type": int // (0 - 4): 0 - "Amazing", 1 - "Pretty Good", 2 - "Okay", 3 - "Pretty Bad", 4 - "Horrible"
            "reason": "..." // Please describe in 25 - 40 words. Please don't use any type of passive in the sentences.
        }
    }
}
"""


SXS_STATEMENT = """
In this project, you will be rating two different responses that are generated for the same prompt in a variety of programming languages. The task contains three main sections.

You will first need to read the prompt that's already provided and will need to answer questions about it.
Then you will look at two AI-generated responses and will rate the quality for each.
Lastly you will be comparing the two responses.


I'll give you one prompt and two responses to that.

1. Select which response do you recommend?

2. Please answer the following questions per response.
- Please rate the model response ("Incorrect" / "Partially Incorrect" / "Completely Correct")
    Completely Correct
        All claims in both the explanation and any code comments are factual and accurate; the code (if any) is functional, safe, and useful.
    Partially correct
        Either or both of the following are true:
            Text: primary claims (central to addressing the prompt) are factual / accurate; secondary claims contain meaningful inaccuracies (or unfounded claims).
                Examples include: an otherwise correct explanation of a library that uses an incorrect link, or a description of a system that misconstrues a small detail of its design.
            Code: has minor problems that are straightforward to fix (e.g., missing imports, small syntax errors), or is correct but has misleading comments.
    Incorrect
        Either or both of the following are true:
            Text: primary claims contain meaningful inaccuracies (or unfounded claims), such that the response is not helpful to the user.
                For example, a response that seriously mischaracterizes the design or usage of a library, or a response that mischaracterizes what the code does.
            Code: has one or more of the following problems:
                Do not use this to flag responses that make simplifying assumptions that a user would reasonably be expected to notice and improve, such as using a hard-coded password in a clearly visible location.
                    Functionality: the program does not compile or run and would require substantial effort to repair.
                    Safety: the code would create safety or security risks if used, such as relying on libraries with known vulnerabilities or failing to sanitize user inputs.
                    Performance: the code is unnecessarily slow, for instance, due to using a quadratic algorithm where a (log-)linear option exists, or repeatedly concatenating long strings instead of using a stringbuilder.
                    Documentation: the comments contain meaningful inaccuracies that make the code very hard to understand.
            Important Note:
                Keep in mind that the code may be functional for the prompter, even if it does not compile or run on your setup. For instance, a response that points to a file only accessible to the prompter, or provides a partial program based on the context provided by the prompter should not be marked as non-functional unless it contains errors that would (likely) manifest in the prompter’s programming context.
- How helpful is this response? ("Not helpful whatsoever" / "Minimally helpful" / "Moderately helpful" / "Very helpful")
    Very helpful
        The user has found what they are looking for entirely within the response.
        All prompt instructions were followed; response delivered fully on the tasks of the prompt.
    Moderately Helpful
        The user may have to use some outside sources to accomplish their goal.
        The response addressed most of the instructions or goal(s) of the prompt, but missed or misinterpreted some small parts.
            For example: a response that describes the right API but assumes a slightly different use-case than what the user articulates.
    minimally helpful
        The response isn't completely off track, but the user does not get much helpful information. The user will have to rely heavily on outside sources.
        The response missed key components of the prompt, rendering it unhelpful to the user.
            For example: a response that discusses a different programming language or library than what the user asked about, or misses a key requirement of the code to be generated.
    Not helpful whatsoever
        The response is not helpful or off-topic. The user is no closer to accomplishing their goal, and the response is completely useless.
            For example: a response that discusses how to grow peaches when asked for a peach pie recipe
- Estimate how long it would take you to answer this prompt starting from this response. (A) If the response is completely unhelpful, your answer should match your estimate from prompt question 3 above (time to answer the prompt from scratch). (B) Enter 0 if the response completely and correctly answers every aspect of the user's prompt.
    Estimate how long, in minutes, it would take you to answer this prompt from scratch (WITH the help of this response) (maximum is 30).
        Using this response, how long would it take you to come up with a very helpful answer for the user?
            If the response is completely unhelpful, your answer should match your estimate from prompt question 3 above (time to answer the prompt from scratch).
            Enter 0 if the response completely and correctly answers every aspect of the user's prompt.
            Otherwise, estimate how much time it would take you to make the necessary changes.
3. And as the result
- Which is better? (1 - 7: 1 - A is much better, 7 - B is much better, 4 - A and B are the same)
- Explain why (e.g: 1. first of all a is ..., 2. Second, ..., ...)
"""
SXS_QUESTION = """
Write the answer in this format (json) to the question I gave you at first. keep the validation format of json. especailly: sxs.why
{
    "sxs": {
        best: "response ...",  \\ "response a" / "response b"
        "response a": {
            "correct": "...", \\ "Incorrect" / "Partially correct" / "Completely correct"
            "helpful": "...", \\ "Not helpful whatsoever" / "Minimally helpful" / "Moderately helpful" / "Very helpful"
            "time": 5 \\ This field is related the response a. How is the response correct and helpful. If the response a is perfect, there is no need to change the response and this field is 0.
        },
        "response b": {
            "correct": "...", \\ "Incorrect" / "Partially correct" / "Completely correct"
            "helpful": "...", \\ "Not helpful whatsoever" / "Minimally helpful" / "Moderately helpful" / "Very helpful"
            "time": 0 \\ This field is related the response b. How is the response correct and helpful. If the response b is perfect, there is no need to change the response and this field is 0.
        },
        "sxs": {
            "rate_which_is_better": 2,    \\ (1 - 7: 1 - A is much better, 7 - B is much better, 4 - A and B are the same) If the best is "response a", this field is smaller than 5 and if "response b", biggr than 3.
            "why": ".." \\ Write the reason in 30 ~ 35 words
        }
    }
}
"""
