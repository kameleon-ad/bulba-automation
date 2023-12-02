document.getElementById('upload').addEventListener('click', () => {
    chrome.tabs.query({active: true, currentWindow: true}, (tabs) => {
        chrome.scripting.executeScript({
            target: {tabId: tabs[0].id},
            function: upload,
        });
    });
});


function upload() {
    let [instruction, prompt, response_a, response_b] = Array
        .from(document.querySelectorAll('[class*="MuiPaper-root-"], [class*="MuiPaper-elevation1-"], [class*="MuiPaper-rounded-"]'))
        .map(element => element.innerHTML);
    let upload_url = 'http://localhost:5000/api/htmls/feedbacks';
    let task_id;
    
    if (!instruction) {
        [instruction, prompt, response_a, response_b] = Array
            .from(document.getElementsByClassName('MuiPaper-root MuiPaper-elevation1 MuiPaper-rounded'))
            .map(element => element.innerHTML);
        upload_url = 'http://localhost:5000/api/htmls/problems';
        const task_id_element = document.querySelector('div > strong + em');
        task_id = task_id_element.textContent.trim();
    } else {
        const task_id_element = document.querySelectorAll('div > strong + em')[1];
        task_id = task_id_element.textContent.trim();
    }
    console.log(instruction, prompt, response_a, response_b);
    
    fetch(upload_url, {
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
        alert("success");
    })
    .catch(error => {
        alert("error");
        console.log(error);
    });
}
