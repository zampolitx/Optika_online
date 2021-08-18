'use strict';
var btn = $('.form_submit');
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
    //let promise = await AJAX();
    var title = $('.add_building_form').val();
    console.log(`это промис ${promise}`);
    console.log(`это title ${title}`);
    return(false);
}

      
document.querySelector('.form_submit').addEventListener('click', async function() {
const answer =  await checkForm();
//const result1 = await Promise.resolve('ok');
console.log(result1);
});


/*$(document).ready(function(){
    btn.click(async function(){
        let answer =  checkForm();
        console.log(`Это answer ${answer}`);
        if(answer==false) {
            
            return false;
        }
        else
            return false;
        //{form.submit();}
    })
})*/