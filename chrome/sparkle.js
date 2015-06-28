new (function() {
    "use strict";

    var knownHashes = null;

    chrome.app.runtime.onLaunched.addListener(function(x) {
        function chooseFilesToGenerateHash() {
            c.chrome.fileSystem.chooseEntry({type:"openFile", acceptsMultiple:!0}, function(b) {
                d = [];
                for (var a = 0;a < b.length;a++) {
                    b[a].file(function(a) {
                        d.push(a);
                        d.length == b.length && l();
                    });
                }
            });
        }
        function generateFileHash(b, a, callbacks) {
            function h() {
                d({total:n, processed:m, ready:n === m});
            }
            function e() {
                var a = p.crypt.byteArrayToHex(g.digest());
                u({hex:a});
            }
            function r() {
                k = m + v;
                k > n && (k = n);
                if (m >= k) {
                    return 0 === k && (h(), e()), !1;
                }
                c = a.slice(m, k);
                l.readAsArrayBuffer(c);
                m = k;
                return!0;
            }
            callbacks = callbacks || {};
            var u = callbacks.ready || function() {
                }, d = callbacks.progress || function() {
                }, n = a.size, v = 1048576, c, m = 0, k = 0;
            if ("undefined" == typeof p.crypt[b]) {
                throw Error('wat "' + b + '"');
            }
            var g = new p.crypt[b], l = new FileReader;
            l.onload = function(a) {
                a = a.target.result;
                h();
                a = new Uint8Array(a);
                g.update(a);
                r() || e();
            };
            r();
        }
        function w(b) {
            function a() {
                var a = e.insertRow(-1), b = a.insertCell(0);
                b.className = "name";
                var d = a.insertCell(1);
                d.className = "hash";
                var c = f.createElement("progress");
                d.appendChild(c);
                this.setName = function(a) {
                    b.innerHTML = "";
                    b.appendChild(f.createTextNode(a));
                };
                this.setProgress = function(a, b) {
                    c.setAttribute("max", b);
                    c.value = a;
                };
                this.setResult = function(hash, title) {
                    var html = hash + " (" + title + ")";
                    d.innerHTML = "";
                    d.appendChild(f.createTextNode(html));
                    h[d.parentNode.rowIndex] = {name:b.firstChild.nodeValue, result:a};
                };
                this.setName(" ");
            }
            var f = b.ownerDocument, h = [], e = f.createElement("table");
            b.appendChild(e);
            this.empty = function() {
                e.innerHTML = "";
            };
            this.getAsText = function() {
                for (var a = "", b = 0;b < h.length;b++) {
                    a += h[b].result + "\t" + h[b].name + "\r\n";
                }
                return a;
            };
            this.add = function() {
                return new a;
            };
        }
        function l() {
            var c = d;
            if (0 == c.length) {
                return!1;
            }
            g = [];
            b.getElementById("startup").style.display = "none";
            b.getElementById("select").style.display = "block";
            var a = b.getElementById("hashList");
            a.style.display = "block";
            a.innerHTML = "";
            s = new w(a);
            b.getElementById("hash").disabled = !0;
            for (a = 0;a < c.length;a++) {
                (function(a) {
                    var c = s.add();
                    c.setName(a.name);
                    generateFileHash(b.getElementById("hash").value, a, {ready:function(hashResult) {
                        var software = knownHashes[hashResult.hex];
                        var title = software ? software.title : "Unknown Software";
                        c.setResult(hashResult.hex, title);
                        g.push(a.name);
                        var progress = b.getElementById("progress");
                        progress.setAttribute("max", d.length);
                        progress.value = g.length;
                        d.length == g.length && (b.getElementById("hash").disabled = !1);
                    }, progress:function(a) {
                        c.setProgress(a.processed, a.total);
                    }});
                })(c[a]);
            }
        }
        var p = null, s = null, b = null, c = null, d = [], g = [];
        chrome.app.window.create("menu.html", {width:900, height:700, frame:"default"}, function(g) {
            c = g.contentWindow;
            b = c.document;
            c.onload = function() {
                p = c.goog;
                b.body.addEventListener("drop", function(a) {
                    d = [];
                    d = a.dataTransfer.files;
                    l();
                    a.stopPropagation();
                    a.preventDefault();
                    return!1;
                }, !1);
                b.body.addEventListener("dragover", function(a) {
                    b.getElementById("dropzone").className = "draghover";
                    a.stopPropagation();
                    a.preventDefault();
                    return!1;
                }, !1);
                b.body.addEventListener("dragleave", function(a) {
                    b.getElementById("dropzone").className = "";
                    a.stopPropagation();
                    a.preventDefault();
                    return!1;
                }, !1);
                b.getElementById("drag").onclick = function() {
                    chooseFilesToGenerateHash();
                };
                b.getElementById("select").onclick = function() {
                    chooseFilesToGenerateHash();
                };
                b.getElementById("hash").onclick = function() {
                    l();
                };
            };
        });
    });

    function init() {
        loadKnownHashes();
    }

    function loadKnownHashes() {
        var xmlhttp = new XMLHttpRequest();
        var url = chrome.runtime.getURL("detector.json");

        xmlhttp.onreadystatechange = function() {
            if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
                var knownHashesArr = JSON.parse(xmlhttp.responseText);
                knownHashes = {};
                for (var i=0; i<knownHashesArr.length; i++) {
                    var hashObj = knownHashesArr[i];
                    knownHashes[hashObj.sha256sum] = hashObj;
                }
            }
        };
        xmlhttp.open("GET", url, true);
        xmlhttp.send();
    }

    init();
})();


