document.getElementById('click-me').addEventListener('click', () => {
    chrome.tabs.query({active: true, currentWindow: true}, (tabs) => {
        chrome.scripting.executeScript({
            target: {tabId: tabs[0].id},
            function: changeBackgroundColor
        });
    });
});

function changeBackgroundColor() {
    console.log(typeof document.body.innerText);
    fetch("http://localhost:5000/api", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams({
            html_content: document.documentElement.innerHTML
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
