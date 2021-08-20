'use strict';
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
const answer = await AJAX();
console.log(`Это answer ${answer}`);
if (answer == 'No') {
    return false;
}
else {
    return btn.submit();
}
});    
    