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
    const clickEvent = new MouseEvent('click', {
        'view': window,
        'bubbles': true,
        'cancelable': true
    });
    const changeEvent = new Event("change", { bubbles: true });
    const category_selector = "span.MuiButtonBase-root.MuiIconButton-root.MuiCheckbox-root.MuiCheckbox-colorPrimary.MuiIconButton-colorPrimary";

    const CODE_RELATED_QUESTION = "Is the prompt code-related? *";
    const CODE_CATEGORY_QUESTION = "Please select the category for the Code-Related Prompt: *";
    const EXPERTISE_LEVEL_QUESTION = "What is your expertise level with the subject(s) of this prompt? *";
    const COMPLEXITY_QUESTION = "In your view, how complex is this prompt? *";

    const A_FOLLOW_INSTRUCTION_QUESTION = "Did the response A follow the instructions it was given in the prompt (both explicit and implicit)?"
    const B_FOLLOW_INSTRUCTION_QUESTION = "Did the response B follow the instructions it was given in the prompt (both explicit and implicit)?"
    const A_TRUTHFUL_CORRECT_QUESTION = "Is Response A truthful and correct? *";
    const B_TRUTHFUL_CORRECT_QUESTION = "Is Response B truthful and correct? *";
    const A_WELL_WRITTEN_QUESTION = "Is Response A well written? *";
    const B_WELL_WRITTEN_QUESTION = "Is Response B well written? *";
    const A_HOW_VERBOSE_QUESTION = "How verbose is Response A?";
    const B_HOW_VERBOSE_QUESTION = "How verbose is Response B?";
    const A_SAFE_QUESTION = "How safe and harmless is Response A? *";
    const B_SAFE_QUESTION = "How safe and harmless is Response B? *";
    const SXS_SCORE_QUESTION = "Side by Side (SxS) Score";
    const SXS_SCORE_EXPLANATION_QUESTION = "SxS Score Explanation *";

    const find_block_by_question = (question) => {
        return Array.from(document.querySelectorAll("span")).find(element => element.innerText === question)?.parentElement.parentElement.parentElement.parentElement;
    }

    const interact_related = (result) => {
        return new Promise ((resolve) => {
            const code_related_ele = document.querySelector("p.MuiFormHelperText-root").parentElement.querySelectorAll("input")[1];
            if (result.category['code-related']) {
                code_related_ele.dispatchEvent(clickEvent);
            } else {
                return;
            }
            return resolve();
        })
    };

    const check_category_select_dep = () => {
        return new Promise((resolve) => {
            const interval_handler = setInterval(() => {
                const elements = document.querySelectorAll(category_selector);
                if (elements.length > 1) {
                    clearInterval(interval_handler);
                    return resolve();
                }
            }, 1000);
        });
    };

    const check_matched_category = (category_expand_ele, result) => {
        return new Promise((resolve) => {
            const setupTimeoutForCategroySelection = () => {
                category_expand_ele.dispatchEvent(clickEvent);
                setTimeout(() => {
                    const target_ele = Array.from(document.querySelectorAll("label.MuiFormControlLabel-root")).find(ele => {
                        return ele.innerText.includes(result.category.category);
                    });
                    if (target_ele) {
                        target_ele.parentElement.querySelector("input").dispatchEvent(clickEvent);
                        return resolve();
                    }
                    setupTimeoutForCategroySelection();
                }, 1000);
            };
            setupTimeoutForCategroySelection();
        });
    };

    const type_and_result_interact = (block=document.createElement("div"), {type, reason}) => {
        block.querySelectorAll("label.MuiFormControlLabel-root")[type].querySelector("input").dispatchEvent(clickEvent);
        if (type > 0 && type < 3) {
            const reason_area = block.nextElementSibling.querySelector("textarea");
            reason_area.value = reason;
            reason_area.dispatchEvent(changeEvent);
        }
    };

    const interact_category = (result) => {
        const category_expand_ele = document.querySelectorAll(category_selector)[1].querySelector("input");
        check_matched_category(category_expand_ele, result).then(() => {
            const truthful_a_ele = find_block_by_question(A_TRUTHFUL_CORRECT_QUESTION);
            const truthful_b_ele = find_block_by_question(B_TRUTHFUL_CORRECT_QUESTION);
            type_and_result_interact(truthful_a_ele, result.truthful_and_correct.A);
            type_and_result_interact(truthful_b_ele, result.truthful_and_correct.B);
        });
    }

    let [_, prompt, response_a, response_b] = Array
        .from(document.getElementsByClassName('MuiPaper-root MuiPaper-elevation1 MuiPaper-rounded'))
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
    }).then(res => res.json())
    .then(result => {
        interact_related(result)
            .then(() => {
                check_category_select_dep()
                    .then(() => {
                        interact_category(result);
                    });
            });
    });
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
