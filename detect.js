var known = {
    en: true, //english
    fa: true, //farsi
    ar: true, //arabic
    zh: true //
};

var lang = (navigator.language || navigator.userLanguage || 'en').substr(0, 2);
if(!known[lang])
    lang = 'en';

// wondershowzen!
$('div.download[lang=' + lang + ']').show();

// hide all the things!
$('div.download[lang!=' + lang + ']').hide();

// do people even read these things
