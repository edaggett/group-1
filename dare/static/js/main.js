function redirect_to_dare() {
	window.location.replace("/dare");
}


function redirect_to_main() {
	window.location.replace("/");
}
function redirect_to_user() {
	window.location.replace("/user");
}

function setup() {
	
    $("#kind").click(redirect_to_dare);

    $('#submissions').click(redirect_to_main);

    $("#user_dare").click(redirect_to_main);

}

$(document).ready(setup)