$(document).ready(function(){
    var btn = $('.form_submit');
    btn.click(function(){
      console.log(get_data(2, 4));
      //console.log(get_data());
      var title = $('.add_building_form').val();
      if(title=='123'){
        return false;
      }
      else
        return false;
        //{form.submit();}
    })
})

function get_data(a, b) {
    $.ajax({
        type: "POST",
        async: false,
        url: "/get_building",
        data: $('form').serialize(),
        type: 'POST',
        success: function(response) {
            var json = jQuery.parseJSON(response);  //Прочитать ответ сервера
            var resp_list = json.resp; //массив с ключем par_buld_resp (из функции get_building main.py)
            console.log(resp_list);
            return a * b;
        },
        error: function(error) {
          console.log(error);
          return 13;
        }
    });
}
