function AJAX(){
    return new Promise(resolve => {
        $.ajax({
            type: "POST",
            url: "/get_building",
            data: $("form").serialize(),
            type: "POST",
            success: function(response) {
                var json = jQuery.parseJSON(response);  //Прочитать ответ сервера
                var resp_list = json.resp; //массив с ключем par_buld_resp (из функции get_building main.py)
                //console.log(resp_list);
                resolve(resp_list);
            },
            error: function(error) {
            console.log(error);
            }
            
        })
        .then(result =>{
            console.log(result);
            return result;
        })
    });
}


$(document).ready(function(){
    var btn = $('.form_submit');
    btn.click(function(){
        var title = $('.add_building_form').val();
        async function my() {
            let result = await AJAX();
            return result;
        }
        let res_my = my();
        console.log(res_my);
        if(title=='123'){
            console.log('no');
            return false;
            }
        else {
            console.log('yes');
            return false;            
        }
            
        //{form.submit();}
    })
})
