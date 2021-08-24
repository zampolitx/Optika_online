async function showAlert (msg, element, success) {
	if (success == true) {
		console.log('alert start')
		element.className = 'alert success';
		element.innerHTML = msg;
		await new Promise((resolve, reject) => {
                    setTimeout(() => {
                    	frm.submit();   //отправляем форму
                    	resolve()
                    }, 3000);
       	});
	}
	else {
		element.className = 'alert error';
		element.innerHTML = msg;
	}
}
	