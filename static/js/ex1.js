const requestURL = '/get_building';
//const requestURL = 'https://jsonplaceholder.typicode.com/users'
function sendRequest(method, url, body = null) {
    return new Promise((resolve, reject) => {
        const xhr = new XMLHttpRequest()
        xhr.open(method, url);
        xhr.responseType = 'json';
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded')
        xhr.onload = () => {
            if (xhr.status >= 400) {
                reject(xhr.response)
            } else {
                resolve(xhr.response)
            }
        }
        xhr.onerror = () => {
            reject(xhr.response)
        }
        xhr.send(body)
    })
    
}

/*const body = "building_name=123"
console.log(typeof body)
console.log(body)
sendRequest("POST", requestURL, body)
.then(data => console.log(data))
.catch(err => console.log(err))*/

let frm = document.forms[0];
frm.onsubmit = function(event) {
    if(frm.building_name.value == '123') {
        event.preventDefault();
        console.log('123 is')
    }
    console.log('click')

}
