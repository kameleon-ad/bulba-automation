document.getElementById('upload').addEventListener('click', () => {
    chrome.tabs.query({active: true, currentWindow: true}, (tabs) => {
        chrome.scripting.executeScript({
            target: {tabId: tabs[0].id},
            function: upload,
        });
    });
});


document.getElementById('solve').addEventListener('click', () => {
    chrome.tabs.query({active: true, currentWindow: true}, (tabs) => {
        chrome.scripting.executeScript({
            target: {tabId: tabs[0].id},
            function: solve,
        });
    });
});


// document.getElementById('upload-problem').addEventListener('click', () => {
//     chrome.tabs.query({active: true, currentWindow: true}, (tabs) => {
//         chrome.scripting.executeScript({
//             target: {tabId: tabs[0].id},
//             function: extract_question_region,
//         });
//     });
// });


function solve() {
    let [_, prompt, response_a, response_b] = Array
        .from(document.querySelectorAll('[class*="MuiPaper-root-"], [class*="MuiPaper-elevation1-"], [class*="MuiPaper-rounded-"]'))
        .map(element => element.innerHTML);
    let api_link = 'http://localhost:5000/api/bulba_v2';

    fetch(api_link, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams({
            prompt,
            response_a,
            response_b,
        }),
        redirect: 'follow',
    }).then(() => {});
}


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
    .then(() => {
        alert("success");
    })
    .catch(error => {
        alert("error");
        console.log(error);
    });
}


function extract_question_region() {
    let [_instruction, prompt, response_a, response_b] = Array
        .from(document.querySelectorAll('[class*="MuiPaper-root-"], [class*="MuiPaper-elevation1-"], [class*="MuiPaper-rounded-"]'))
        .map(element => element.innerHTML);
    const question_group = document.querySelector('[class*=MuiTree]').children[1];
    const keywords = [
        "both explicit and implicit",
        "truthful and correct?",
        "well written?",
        "How verbose is",
        "safe and harmless",
    ];
    // let tmp_keywords = [...keywords];
    question_group
        .childNodes
        .forEach(child => {
            const target_node = Array.from(child.children).pop().childNodes[0].childNodes[0].childNodes[0];
            const question_ele = target_node.childNodes[0];
            const answer_ele = target_node.childNodes[1];
            const question = question_ele.innerText.trim();
            const answer = answer_ele.innerText.trim();
            // if (tmp_keywords.findIndex(keyword => {
            //     if (!question.includes(keyword)) {
            //         return false;
            //     }
            //     tmp_keywords = tmp_keywords.filter(one => one != keyword)
            //     return true;
            // }) != -1) {
            //     fetch("http://127.0.0.1:5000/api/questions", {
            //         method: 'POST',
            //         headers: {
            //             'Content-Type': 'application/x-www-form-urlencoded',
            //         },
            //         body: new URLSearchParams({
            //             question,
            //         }),
            //         redirect: 'follow'
            //     })
            //     .then(response => response.json())
            //     .then(() => {
            //         alert("success");
            //     })
            //     .catch(error => {
            //         alert("error");
            //         console.log(error);
            //     });
            // }
            const keyword = keywords.find(keyword => question.includes(keyword));
            if (keyword) {
                pl = true;
                let response = question.includes("esponse A") ? response_a : response_b;
                fetch("http://127.0.0.1:5000/api/answers", {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded',
                    },
                    body: new URLSearchParams({
                        question,
                        response,
                        answer,
                        prompt,
                    }),
                    redirect: 'follow'
                })
                .then(response => response.json())
                .then(() => {
                    alert("success");
                })
                .catch(error => {
                    alert("error");
                    console.log(error);
                });
            }
        });
}
