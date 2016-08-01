function redirect_to_dare() {
	window.location.replace("/dare");
}

function you_submitted() {
	$('radio').click(alert('You have submitted'));
}

function setup() {
	//alert("javascript is here!");
    $("#kind").click(redirect_to_dare);
}

$(document).ready(setup)