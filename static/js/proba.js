'use strict';

const requestURL = '/get_building';
let frm = document.forms[0];
let but = frm.elements[1];
but.onclick = async function(event) {
    let body = 'building_name=' + frm.building_name.value;    //получаем 'building_name=123', Если ввели в форму 123
    
    let answer = AJAX("POST", requestURL, body)
    answer.then(data => {
        if(data.resp=='New'){
            console.log('Новое здание');
            frm.submit();
        }
        else {
            console.log('Старое здание');
        }
    })
    .catch(err => console.log(err))
}

function AJAX(method, url, body = null) {
    return new Promise((resolve, reject) => {
        const xhr = new XMLHttpRequest()
        xhr.open(method, url);
        xhr.responseType = 'json';
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded')
        xhr.onload = () => {
            if (xhr.status >= 400) {
                reject(xhr.response)
            } else {
                resolve(xhr.response)
            }
        }
        xhr.onerror = () => {
            reject(xhr.response)
        }
        xhr.send(body)
    })
    
}