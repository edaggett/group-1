function redirect_to_dare() {
	window.location.replace("/dare");
}


function setup() {
	alert("javascript is here!");
    $("#kind").click(redirect_to_dare);
}

$(document).ready(setup)