function get_parlor() {
    $.ajax({
        type: "POST",
        url: "/get_parlor",
        data: $('form').serialize(),
        type: 'POST',
        success: function(response) {
            $('.par').empty();  //Удалить старые записи из списка
            var json = jQuery.parseJSON(response);  //Прочитать ответ сервера
            var resp_list = json.par_buld_resp; //массив с ключем par_buld_resp (из функции get_parlor main.py)
            console.log(resp_list);
            var option = '';
            for (var i=0; i<resp_list.length; i++){ //по количеству элементов в массиве
                option += '<option value="'+resp_list[i] + '">' + resp_list[i] + '</option>';   //формируем строку html типа <option value="two">one</option>
                //$('<option/>').val(resp_list[i]).html(resp_list[i]).appendTo('.par');
            }
            $('.par').append(option);
            //var json = jQuery.parseJSON(response);
            //$('#mydiv').html(json.par_buld_resp); //par_buld_resp - название ключа из main.py
        },
        error: function(error) {
            console.log(error);
        }
    });
}