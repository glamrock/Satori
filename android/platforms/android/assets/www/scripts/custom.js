// JavaScript Document

$(document).ready(function(){

	$('.change-style').click(function(){
		$('.styles').toggle(200);
	});
	
	$('.styles a').click(function(){
		snapper.open('left');
	});
	
	var snapper = new Snap({
	  element: document.getElementById('content')
	});

	$('.close-sidebar').click(function(){
		snapper.close();
		//$('.deploy-sidebar').removeClass('remove-sidebar');
	});

	

	$('.deploy-sidebar').click(function(){
		//$(this).toggleClass('remove-sidebar');
		if( snapper.state().state=="left" ){
			snapper.close();
		} else {
			snapper.open('left');
		}
		return false;
	});

	
});