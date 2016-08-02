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
    if (#submissions==True):
    	window.alert("You completed the dare! Your points have been recorded")
    else:
    	window.alert("Go try out the dare and spread a little kindness!")
    $('#submissions').click(redirect_to_main);

    $("#user_dare").click(redirect_to_main);

}

$(document).ready(setup)