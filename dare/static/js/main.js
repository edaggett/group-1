function redirect_to_dare() {
	window.location.replace("/dare");
}


function redirect_to_main() {
	window.location.replace("/");
}


function setup() {
	
    $("#kind").click(redirect_to_dare);

    $('#submissions').click(redirect_to_main);

}

$(document).ready(setup)