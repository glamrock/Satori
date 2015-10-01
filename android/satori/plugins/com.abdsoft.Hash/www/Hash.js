window.hashString = function(str, callback) {
        cordova.exec(callback, function(err) {
            callback('Nothing to hashString.');
        }, "Hash", "hashString", [str]);
    };

window.hashFile = function(str, callback) {
        cordova.exec(callback, function(err) {
            callback('Nothing to hashFile.');
        }, "Hash", "hashFile", [str]);
    };
