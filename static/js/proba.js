"use strict";
var xhr = new XMLHttpRequest();
xhr.open("POST", "http://localhost:5000/proba", true);
let js = {"my":"second"};
xhr.send(js);
xhr.onload = function() {
	console.log(xhr.status);
	console.log(xhr.response);
	console.log(xhr);
}