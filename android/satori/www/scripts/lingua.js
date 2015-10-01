jQuery(document).ready(function () {
    
    jQuery(".lingua").hide();
    jQuery(".lingua_dl").hide();
	/*jQuery(".lingua").click(function () {
        jQuery(".lingua_dl").not(jQuery(this).next(".lingua_dl")).hide();
        jQuery(this).next(".lingua_dl").toggle();
    });
    jQuery('.lingua:first-child').trigger('click');
	*/
	
	$( "select" ).change( displayVals );
	displayVals();
});

function displayVals() {
	var laValue = $( "#language" ).val();
	jQuery(".lingua_dl").not(jQuery("#"+laValue).next(".lingua_dl")).hide();

	jQuery("#"+laValue).next(".lingua_dl").show();
  
}