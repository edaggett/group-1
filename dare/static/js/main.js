function redirect_to_dare() {
	window.location.replace("/dare");
}

function redirect_to_main() {
	window.location.replace("/");
}
// function you_submitted() {
// 	$('#radio').click(redirect_to_dare);
// 	alert('You have submitted')
// }

function setup() {
	//alert("javascript is here!");
    $("#kind").click(redirect_to_dare);
    $('#submissions').click(redirect_main);
	if completed_dare=True:
		alert('You have submitted')
}

$(document).ready(setup)