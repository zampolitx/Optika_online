'use strict';

const requestURL = '/get_building';
let frm = document.forms[0];
let but = frm.elements[1];
but.onclick = async function(event) {
    let building_name = frm.building_name.value;
    let body = 'building_name=' + building_name;    //получаем 'building_name=123', Если ввели в форму 123
    if (building_name == '') {
        console.log('Пустая строка');
        return false;
    }
    let answer = AJAX("POST", requestURL, body)
    answer.then(data => {
        console.log(typeof(data.resp));
        console.log(data.resp);
        if(data.resp=='Old'){
            console.log('Старое здание');
        }
        else {
            console.log('Новое здание здание');
            alert('new2')
            frm.submit();
        }
    })
    .catch(err => console.log(err))
}

