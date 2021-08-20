var btn = document.querySelector('.form_submit');
btn.addEventListener('click', async function() {
const answer = await AJAX();
console.log(`Это answer ${answer}`);
if (answer == 'No') {
    return false;
}
else {
    return false;
}
});

function AJAX() {
    console.log($('.form_add').serialize());
    return new Promise(function(resolve, reject){
        let a = 4 + 4;
        function(response) {
            let resp_list = 'NNNN';
            resolve(resp_list);
        },
        function(error) {
          console.log(`Это AJAX error ${error}`);
          reject(error);
        }
    });
    }