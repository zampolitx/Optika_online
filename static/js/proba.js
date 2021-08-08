$(document).ready(function(){
	var btn = $('.form_submit');
	btn.click(function(){
		console.log('Начало выполнения главной функции');
		$.when(get_data()).done(function(a1){
			var res = a1[0];
			console.log(res);
		})
	})
});


function get_data() {
    $.ajax({
        type: "POST",
        url: "/get_building",
        data: $('form').serialize(),
        type: 'POST',
        success: function(response) {
					console.log('Запуск ajax');
            var json = jQuery.parseJSON(response);  //Прочитать ответ сервера
            var resp_list = json.resp; //массив с ключем par_buld_resp (из функции get_building main.py)
            return resp_list;
        },
        error: function(error) {
          console.log(error);
        }
    });
}
