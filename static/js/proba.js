'use strict';
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
            //console.log(resp_list);
            resolve(resp_list);
        },
        error: function(error) {
          console.log(error);
          reject(error);
        }
    });
    })
}
var a = 1;
$(document).ready(function(){
    var btn = $('.form_submit');
    btn.click(function(){
      let promise = AJAX();
      promise.then(function(result){
        console.log(typeof(a));
        console.log(a);
        a= result;
        console.log(typeof(a));
        console.log(a);
      }).then(function(result){
        console.log(`Второй log ${a}`);
      });

      var title = $('.add_building_form').val();
      if(title=='123'){
        return false;
      }
      else
        return false;
        //{form.submit();}
    })
})
