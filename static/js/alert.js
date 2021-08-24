function showAlert (msg, element, success) {
	return new Promise((resolve, reject) => {
		console.log('alert');
		if (success == true) {
			console.log('alert start')
			element.className = 'alert success';
			element.innerHTML = msg;
                setTimeout(() => {
                	resolve()
            	    }, 3000);

		}
		else {
			element.className = 'alert error';
			element.innerHTML = msg;
		}
	})
}
	