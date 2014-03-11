var known = {
    en: true,
    fa: true,
    ar: true,
    zh: true
};

var lang = (navigator.language || navigator.userLanguage || 'en').substr(0, 2);
if(!known[lang])
    lang = 'en';

// wondershowzen!
$('div.download[lang=' + lang + ']').show();

// hide all the things!
$('div.download[lang!=' + lang + ']').hide();


