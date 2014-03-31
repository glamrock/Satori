jQuery(document).ready(function () {
    
    jQuery(".lingua_dl").hide();
    jQuery(".lingua").click(function () {
        jQuery(".lingua_dl").not(jQuery(this).next(".lingua_dl")).hide();
        jQuery(this).next(".lingua_dl").toggle();
    });
    jQuery('.lingua:first-child').trigger('click');
});
