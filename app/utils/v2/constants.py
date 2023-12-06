BASIC_MESSAGES = [
    {"role": "system", "content": "You are a helpful assistant."},
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
| Code Modication - Fix | Specify defective code and ask the model to fix it. This includes fixing formatting and style.  | Fix this code #!/bin/bash # Enable the Firewall sudo /usr/libexec/ApplicationFirewall/socketfilterfw --setglobalstate on # Check if the Firewall is enabled firewall_status=$(sudo /usr/libexec/ApplicationFirewall/socketfilterfw --getglobalstate) if [[ "$firewall_status" == "Firewall is enabled. (State = 1)" ]]; then echo "Firewall is enabled" else echo "Failed to enable Firewall" fi |
| Code Modication - Optimization | Specify code and ask the model to improve its performance. | Please help me optimize the following bigquery SQL query: WITH import_data AS ( SELECT id, ref_date, day FROM test-zsuite.catalunya.revenue__import_pms_data WHERE ref_date IN ('2023-08-28', '2023-09-04', '2023-09-11') AND day = '2023-09-11' AND band_room = 'BASE-A' ) SELECT *  FROM import_data ORDER BY ref_date, day, band_room; |
| Code Modication - Other  | Specify code and ask the model to change it.   | SELECT DISTINCT    RTRIM(ISNULL(Userfield1, '')) AS FieldtypeFROM    tblclient    LEFT JOIN fngetsplit(@ClientCust, '') AS UseCust ON tblclient.ClientCust = UseCust.ValueWHERE    RTRIM(ISNULL(Userfield1, '')) <> ''    AND tblclient.Clientclosed = 'N'UNIONSELECT DISTINCT    RTRIM(ISNULL(Userfield2, '')) AS FieldtypeFROM    tblclient    LEFT JOIN fngetsplit(@ClientCust, '') AS UseCust ON tblclient.ClientCust = UseCust.ValueWHERE    RTRIM(ISNULL(Userfield2, '')) <> ''    AND tblclient.Clientclosed = 'N'UNIONSELECT DISTINCT    RTRIM(ISNULL(Userfield3, '')) AS FieldtypeFROM    tblclient    LEFT JOIN fngetsplit(@ClientCust, '') AS UseCust ON tblclient.ClientCust = UseCust.ValueWHERE    RTRIM(ISNULL(Userfield3, '')) <> ''    AND tblclient.Clientclosed = 'N';simplify this |
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
CODE_RELATED_AND_CATEGORY_QUESTION = """
I gave you one prompt. Please determine if is this prompt code-related.
And if so also determine the category of the above prompt and the clarity of the prompt.
The output is json format
{
    "code-related": "..." // 0 / 1 : 0 - non-related, 1 - code-related
    "category": "..." // "Code Understanding" / "Code Execution" / "Code Translation" / ...
    "clarity": ... // 0 - 2: 0 - Completely Clear, 1 - Vague/Ambiguous, 2 - Missing Context
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
    "A": { // The result for The Response B.
        "type": int // (0 - 4): 0 - "No Issues", 1 - "Minor Issues", 2 - "Major Issues", 3 - "Cannot Assess", 4 - "N/A"
        "reason": ... // If the type is (0) No Issues, in that case, there is no need to use "reason" field. Also "B" is same with this.
    },
    "B": { // The result for The Response A.
        "type": int, // (0 - 4): 0 - "No Issues", 1 - "Minor Issues", 2 - "Major Issues", 3 - "Cannot Assess", 4 - "N/A"
        "reason": "..." // If the type is not No Issues, in that case please describe in 20 - 40 words.
    }
}
"""
