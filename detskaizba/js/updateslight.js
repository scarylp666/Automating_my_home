function sendRequest() {
	const xhr = new XMLHttpRequest();

	xhr.onreadystatechange = function () {
		if (xhr.readyState === 4 && xhr.status === 200) {
			const response = xhr.responseText;
			console.log(response);
			const parser = new DOMParser();
			const doc = parser.parseFromString(response, "application/xml");
			const ac = doc.getElementsByTagName("ac")[0];
			const clr = doc.getElementsByTagName("cl")[0];
			const clg = doc.getElementsByTagName("cl")[1];
			const clb = doc.getElementsByTagName("cl")[2];
			const nl = doc.getElementsByTagName("nl")[0];
			document.getElementById("toparse").innerHTML = response;
			document.getElementById("brightness").innerHTML = ac.textContent;
			document.getElementById("red").innerHTML = clr.textContent;
			document.getElementById("green").innerHTML = clg.textContent;
			document.getElementById("blue").innerHTML = clb.textContent;
			document.getElementById("timer").innerHTML = nl.textContent;
			console.log(clg.textContent);
		}
	};

	xhr.open("GET", "http://192.168.1.100/win", true);
	xhr.send();
}
setInterval(sendRequest, 5000);
