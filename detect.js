var known = {
    en: true,
    fa: true,
    ar: true,
    zh: true
};

var lang = (navigator.language || navigator.userLanguage || 'en').substr(0, 2);
if(!known[lang])
    lang = 'en';

$('div.wrapper[lang=' + lang + ']').show();

$('div.wrapper[lang!=' + lang + ']').hide();
