# Did The Response Follow The Instructions It Was Given By The Prompt Both Implicitly And Explicitly

Focus on whether the response reflects the instructions and goals of the prompt, not on truthfulness or correctness issues (e.g., bad code, poor explanation) – those rated below.

Use the following rubric:

| Option     | Description                                                                                     | Explanation        |
|------------|-------------------------------------------------------------------------------------------------|--------------------|
| No Issues  | All prompt instructions were followed; response delivered fully on the tasks of the prompt.       | Nor required       |
| Minor Issues | The response addressed most of the instructions or goal(s) of the prompt, but missed or misinterpreted some small parts. <ul><li>For example: a response that describes the right API but assumes a slightly different use-case than what the user articulates.</li></ul> | Required if issues are found. Describe what aspects of the prompt the response missed or misinterpreted. |
| Major Issues | The response missed key components of the prompt, rendering it unhelpful to the user. <ul><li>For example: a response that discusses a different programming language or library than what the user asked about, or misses a key requirement of the code to be generated.</li></ul> | Required if issues are found. Describe what aspects of the prompt the response missed or misinterpreted. |
| N/A        | There are no explicit or implicit instructions to follow in the prompt or the response is canned (e.g. the model states it cannot do it). | Not required       |
