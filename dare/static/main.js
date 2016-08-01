function redirect_to_advice() {
	window.location.replace("/dare");
}


function setup() {
	alert("javascript is here!");
    $("#kind").click(redirect_to_advice);
}

$(document).ready(setup)