$(document).ready(function(){
    var form=$(this), btn = form.find('.form_submit');
    setInterval(function(){
      //alert('exit setInterval');
    }, 3000);
    btn.click(function(){
      var title = $('.add_building_form').val();
      console.log(title);
      if(title=='123'){
        return false;
      }
      else
        {form.submit();}
    })
})
