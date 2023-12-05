BASIC_MESSAGES = [
    {"role": "system", "content": "You are a helpful assistant."},
]


CATEGORY_STATEMENT = """
#  Selecting The Category For The Code Related Prompt

What is the code use case this prompt falls under? (Only if the prompt is code related)

| Use Case Option   | Description   | Example Prompt   |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Code Understanding | Provide code and ask questions about it including code review style critique. If the prompt is just code with no ask, select this use case. | How many times count++ will run? for (int i = 1; i<= n; i++) for (int j = 1; j <= n; j= j\*2) count++; |
| Code Execution | Execute code and display the results. (Note that this wouldn’t account for implicit code execution for instance converting data from one format to other | Run this code: a = 1 b = "3" print(a+b) |
| Code Translation  | Translate code into another programming language. | I have this snippet in Java: \`\`\`\` please convert it to Kotlin.   |
| Code Modication - Fix | Specify defective code and ask the model to fix it. This includes fixing formatting and style.  | Fix this code #!/bin/bash # Enable the Firewall sudo /usr/libexec/ApplicationFirewall/socketfilterfw --setglobalstate on # Check if the Firewall is enabled firewall_status=$(sudo /usr/libexec/ApplicationFirewall/socketfilterfw --getglobalstate) if [[ "$firewall_status" == "Firewall is enabled. (State = 1)" ]]; then echo "Firewall is enabled" else echo "Failed to enable Firewall" fi |
| Code Modication - Optimization | Specify code and ask the model to improve its performance. | Please help me optimize the following bigquery SQL query: WITH import_data AS ( SELECT id, ref_date, day FROM test-zsuite.catalunya.revenue__import_pms_data WHERE ref_date IN ('2023-08-28', '2023-09-04', '2023-09-11') AND day = '2023-09-11' AND band_room = 'BASE-A' ) SELECT *  FROM import_data ORDER BY ref_date, day, band_room; |
| Code Modication - Other  | Specify code and ask the model to change it.   | SELECT DISTINCT    RTRIM(ISNULL(Userfield1, '')) AS FieldtypeFROM    tblclient    LEFT JOIN fngetsplit(@ClientCust, '') AS UseCust ON tblclient.ClientCust = UseCust.ValueWHERE    RTRIM(ISNULL(Userfield1, '')) <> ''    AND tblclient.Clientclosed = 'N'UNIONSELECT DISTINCT    RTRIM(ISNULL(Userfield2, '')) AS FieldtypeFROM    tblclient    LEFT JOIN fngetsplit(@ClientCust, '') AS UseCust ON tblclient.ClientCust = UseCust.ValueWHERE    RTRIM(ISNULL(Userfield2, '')) <> ''    AND tblclient.Clientclosed = 'N'UNIONSELECT DISTINCT    RTRIM(ISNULL(Userfield3, '')) AS FieldtypeFROM    tblclient    LEFT JOIN fngetsplit(@ClientCust, '') AS UseCust ON tblclient.ClientCust = UseCust.ValueWHERE    RTRIM(ISNULL(Userfield3, '')) <> ''    AND tblclient.Clientclosed = 'N';simplify this |
| Code Debug - Error | Provide an error and (optional) code ask the model to what it means or how to resolve it.   | PS C:\\Users\\WeiJie\\PycharmProjects> python -m venv ll_envError: Command '['C:\\\\Users\\\\WeiJie\\\\PycharmProjects\\\\ll_env\\\\Scripts\\\\python.exe', '-m', 'ensurepip', '--upgrade', '--default-pip']' returned non-zero exit status 1.  |
| Code Generation - Tests  | Generate tests, for given code.   | Generate four unit tests for a C# functionCountDatesMatchingToday(List<DateTime> dates) that counts how many dates on the input list fall on the same day of the week as today. Test with an empty list, list with some matches, list with no matches, and a list with all elements matching. Make sure the tests are robust and work independently of when they are run. |
| Code Generation - Comments  | Add comments and/or documentation.   | Add docstrings to this function….  |
| Code Generation - Other  | Generate code to perform a certain task. | write a bash script to delete all directories named 'node_modules' and their contents from each directory in the current directory |
| Code Learning  | Provide guidance on how to learn programming language concepts, explanations for terms, questions about APIs.   | In Flask project I set up a route '/'. How can I let visitor download all website required files and then render index.html from their local ?\`   |
| Code Recommendations  | Provide recommendations on which libraries or programming patterns to use   | What is the best library in python for hierarchical DBSCAN?   |
| Data Conversion   | Convert from one data format to another. | [    {        id: 1,        title: "JavaScript",        course: "Web Development",        isActive: true    },    {        id: 2,        title: "React",        course: "Frontend Development",        isActive: false    },    {        id: 3,        titile: "Node",        course: "Backend Development",        isActive: true    }]Convert this into json format |
"""
CATEGORY_QUESTION = """
I gave you one prompt. Please determine the category of the above prompt.
The output is json format
{
    "category": "..." // "Code Understanding" / "Code Execution" / "Code Translation" / ...
}
"""
