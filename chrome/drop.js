document.getElementById('lingua').addEventListener('change', function () {
    Array.prototype.forEach.call(document.querySelectorAll('.lingua_dl'),  function (e) {
        e.style.display = 'none';
    });
    var sel = +this.selectedIndex - 2;
    if (sel >= 0) {
        document.getElementById('lingua_head').style.display = 'block';
        document.getElementById(sel).style.display = 'block';
    }
    else {
        document.getElementById('lingua_head').style.display = 'none';
    }
});
