document.getElementById('click-me').addEventListener('click', () => {
    chrome.tabs.query({active: true, currentWindow: true}, (tabs) => {
        chrome.scripting.executeScript({
            target: {tabId: tabs[0].id},
            function: upload_problem,
        });
    });
});

function upload_problem() {
    const [instruction, prompt, response_a, response_b] = Array
        .from(document.getElementsByClassName("MuiPaper-root MuiPaper-elevation1 MuiPaper-rounded"))
        .map(element => element.innerHTML);
    
    const task_id_element = document.querySelector('div > strong + em');
    const task_id = task_id_element.textContent.trim();

    fetch("http://localhost:5000/api/bulba/openai", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams({
            task_id,
            html_content: document.documentElement.innerHTML,
            instruction,
            prompt,
            response_a,
            response_b,
        }),
        redirect: 'follow'
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
    })
    .catch(error => {
        console.error('Error', error);
    });
}
