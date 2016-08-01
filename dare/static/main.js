<<<<<<< HEAD
<<<<<<< HEAD
<button onclick = "window.location.href='dare.html'">Continue</button>
=======
function redirect_to_advice() {
=======
function redirect_to_dare() {
>>>>>>> origin/master
	window.location.replace("/dare");
}


function setup() {
	alert("javascript is here!");
    $("#kind").click(redirect_to_dare);
}

$(document).ready(setup)
>>>>>>> origin/master
