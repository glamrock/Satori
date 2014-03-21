var known = {
    en: true, //english
    fa: true, //farsi
    ar: true, //arabic
    zh: true, //chinese
    ru: true, //russian
    vi: true, //vietnamese
    es: true, //spanish
    it: true, //italian
    ko: true, //korean
    pl: true, //polish
    nl: true, //dutch
    de: true, //german
    pt: true //portuguese
};

var lang = (navigator.language || navigator.userLanguage || 'en').substr(0, 2);
if(!known[lang])
    lang = 'en';

// wondershowzen!
$('div.download[lang=' + lang + ']').show();

// hide all the things!
$('div.download[lang!=' + lang + ']').hide();

// do people even read these things
