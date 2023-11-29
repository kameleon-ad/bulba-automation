document.getElementById('click-me').addEventListener('click', () => {
    chrome.tabs.query({active: true, currentWindow: true}, (tabs) => {
        chrome.scripting.executeScript({
            target: {tabId: tabs[0].id},
            function: changeBackgroundColor
        });
    });
});

function changeBackgroundColor() {
    const [instruction, prompt, response_a, response_b] = Array
        .from(document.getElementsByClassName("MuiPaper-root MuiPaper-elevation1 MuiPaper-rounded"))
        .map(element => element.innerHTML);

    fetch("http://localhost:5000/api/bulba/openai", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams({
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
