'use strict';

const requestURL = '/get_AJAX';
let frm = document.forms[0];
let but = frm.elements[6];
but.onclick = async function(event) {
    let alert_div = document.querySelector('.alert');   // элемент с сообщением

    let room_name = frm.room_name.value;
    let body = 'room_name=' + room_name;        // Получаем 'room_name=123', Если ввели в форму 123
    if (room_name == '') {                          // Если введена пустая строка в форму
        showAlert('Заполните форму ниже!', alert_div, false)
        .then( () =>  console.log('Пустая строка ввода'))
        return false;
    }

    let answer = AJAX("POST", requestURL, body)         // Обращаемся к БД

    answer.then(function (data) {
        if(data.resp=='Old'){                           // Если в БД есть такая запись
            showAlert('Запись уже есть', alert_div, false)
            .then( () =>  console.log('Запись уже есть'))
            return false;
        }
        else {                                          // Если в БД нет такой записи
            showAlert('Данные отправлены', alert_div, true)
            .then(() => frm.submit());
        }
    })
    .catch(err => console.log(err))
}