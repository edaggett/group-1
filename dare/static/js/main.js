function redirect_to_dare() {
	window.location.replace("/dare");
}

$("p").mouseenter(function(){
}

function redirect_to_main() {
	window.location.replace("/");
}
function redirect_to_user() {
	window.location.replace("/user");
}
function submit_alert(){
		if ($("#didDare").prop("checked")){
    	window.alert("You completed the dare! Your points have been recorded")
    	}
    	else{
    	window.alert("Go try out the dare and spread a little kindness!")}}

function setup() {

    $("#kind").click(redirect_to_dare);
   

    $('#submissions').click(redirect_to_main);
<<<<<<< HEAD

    


// if {
//     	window.alert("You completed the dare! Your points have been recorded")
//     }
//     else{
//     	window.alert("Go try out the dare and spread a little kindness!")
//     }
=======
  	$("#dareForm").submit(submit_alert);
		
     
>>>>>>> origin/master
    $("#user_dare").click(redirect_to_main);

}

$(document).ready(setup)