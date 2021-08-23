/*'use strict';
let promise = new Promise(function(resolve, reject){
	let a = 4/2;
	setTimeout(() => resolve(a), 3000);
});

console.log(promise);
promise.then(console.log());*/

/*$(document).ready(function(){
    var btn = $('.form_submit');
    btn.click(function(){
      var answer = get_data();
      var title = $('.add_building_form').val();
      if(title==''){
        return false;
      }
      else
        return false;
        //{form.submit();}
    })
})

function get_data() {
    $.ajax({
        type: "POST",
        url: "/get_building",
        data: $('form').serialize(),
        type: 'POST',
        success: function(response) {
            var json = jQuery.parseJSON(response);  //Прочитать ответ сервера
            var resp_list = json.resp; //массив с ключем par_buld_resp (из функции get_building main.py)
            console.log(resp_list);
            return resp_list;
        },
        error: function(error) {
          console.log(error);
          return error;
        }
    });
}*/

/*'use strict';
var btn = document.querySelector('.form_submit');
function AJAX() {
    return new Promise(function(resolve, reject){
        $.ajax({
        type: "POST",
        url: "/get_building",
        data: $('form').serialize(),
        type: 'POST',
        success: function(response) {
            var json = jQuery.parseJSON(response);  //Прочитать ответ сервера
            var resp_list = json.resp; //массив с ключем par_buld_resp (из функции get_building main.py)
            console.log(`Это resp_list ${resp_list}`);
            resolve(resp_list);
        },
        error: function(error) {
          console.log(error);
          reject(error);
        }
    });
    })
}

async function checkForm() {
    let promise = await AJAX();
    var title = $('.add_building_form').val();
    if (title == '') {
        return 'No'
    }
    try {
    let promise = await AJAX();
    console.log(`это промис ${promise}`);
    console.log(`это title ${title}`);
    if (promise == 'Old') {
        return 'No'
    }
} catch (error) {
    console.log(`это error checkForm ${error}`);
}
    return('No');
}



btn.addEventListener('click', async function() {
const answer = await checkForm();
console.log(`Это answer ${answer}`);
if (answer == 'No') {
    return false;
}
else {
    return btn.submit();
}
});*/


/*
let building_name = 'bnxgcxgh';

// Создаем экземпляр класса XMLHttpRequest
const request = new XMLHttpRequest();

// Указываем путь до файла на сервере, который будет обрабатывать наш запрос 
const url = "/get_building";
 
// Так же как и в GET составляем строку с данными, но уже без пути к файлу 
const params = "building_name=" + building_name;
 
// Указываем что соединение у нас будет POST, говорим что путь к файлу в переменной url, и что запрос у нас
//асинхронный, по умолчанию так и есть не стоит его указывать, еще есть 4-й параметр пароль авторизации, но этот
//    параметр тоже необязателен.
request.open("POST", url, true);
 
//В заголовке говорим что тип передаваемых данных закодирован. 
request.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
 
request.addEventListener("readystatechange", () => {

    if(request.readyState === 4 && request.status === 200) {       
        console.log(request.responseText);
    }
});
 
//  Вот здесь мы и передаем строку с данными, которую формировали выше. И собственно выполняем запрос. 
request.send(params);

*/