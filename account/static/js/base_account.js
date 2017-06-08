$(document).ready(function(){
	
	$('#loginForm').on('submit',function(evt){
		evt.preventDefault();
		var formArray = $(this);
		for(var i in formArray[0]){
			console.log(i+":"+formArray[0][i])
		}
		
	});





});