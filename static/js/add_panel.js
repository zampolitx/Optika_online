"use strict";
var mydata = JSON.parse(document.getElementById("mydiv").dataset.parent);
console.log(mydata.Корпус1);
console.log(Object.keys(mydata));
let xhr = new XMLHttpRequest();
xhr.open("post", "http://localhost:5000/add_panel", true);
xhr.responseType = 'json';
xhr.send();
xhr.onload = function() {
	let responseObj = xhr.response;
	console.log(xhr.statusText);
}
