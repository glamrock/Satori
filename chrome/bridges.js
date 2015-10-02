$(document).ready(function() {
    var bridges = new Array('<input class="getacross" value="obfs3 192.36.27.73:57307 01A95FF9C3C7276C8D18889A102F86026A679026">',
'<input class="getacross" value="obfs3 194.132.209.97:42356 8AE7001B106E453B4CC973C4D1EB76D6772B350A">',
'<input class="getacross" value="obfs3 23.95.27.37:49209 3BDCDFE8E83B24331B58471450FFFA2B79A6B9AC">',
'<input class="getacross" value="obfs3 45.33.80.72:37868 C058186571C5448AAE27B402150DCBCCC1ADAC1F">',
'<input class="getacross" value="obfs3 192.36.27.254:58476 FBF8C2BB73753A5075306A624C5C4D605DCD502D">',
'<input class="getacross" value="obfs3 83.212.117.231:54185 B687A4B74920A7842B676C0C300D7119FB5F7E24">',
'<input class="getacross" value="37.139.80.10:9001 8CD7E6DE9E0DC3A281FE997CB73022D948047B6E">',
'<input class="getacross" value="37.138.83.202:443 EF2CB29C5E440D61DEA21E9C357BE962503C6D0F">');
    var randno = Math.floor(Math.random()*(bridges.length));
    $('.bridge').append(bridges[randno]);
    console.log(randno);
});

