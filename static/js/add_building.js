'use strict';

const requestURL = '/get_building';
let frm = document.forms[0];
let but = frm.elements[1];
but.onclick = async function(event) {
    let alert_div = document.querySelector('.alert');

    let building_name = frm.building_name.value;
    let body = 'building_name=' + building_name;    //получаем 'building_name=123', Если ввели в форму 123
    if (building_name == '') {
        alert_div.className = 'alert error';
        alert_div.innerHTML = "<strong> Заполните поле ввода </strong>";
        console.log('Пустая строка');
        return false;
    }
    let answer = AJAX("POST", requestURL, body)
    answer.then(function (data) {
        console.log(typeof(data.resp));
        console.log(data.resp);
        if(data.resp=='Old'){
            alert_div.className = 'alert error';
            alert_div.innerHTML = "<strong> Запись уже есть </strong>";
            showAlert('Здание уже есть', alert_div, success=false);
            console.log('Старое здание');
        }
        else {
            async function na() {       //Функция для задержки перед отправкой формы
                alert_div.className = 'alert success'       //Применяем стиль alert.success
                alert_div.innerHTML = "<strong> Запись добавлена</strong>"  //Выводим сообщение
                await new Promise((resolve, reject) => {
                    setTimeout(() => {
                    frm.submit();   //отправляем форму
                    resolve()
                    }, 3000);
                });
            }
            na();
        }
    })
    .catch(err => console.log(err))
}

