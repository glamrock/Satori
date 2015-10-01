Hash plugin for Cordova / PhoneGap
==================================

This Plugin is used to generate hash (md5, sha1, sha-256, sha-384, sha-512) of any file or string.

## Usage:
    Parameters (Object): {data: file/string, hash: hash algorithm}
    data:
      file: "/mnt/sdcard/..." (Path to the file);
      string: "Hello World!"
    hash: md5, sha1, sha-256, sha-384, sha-512

## Example Usage: 
	Example String: window.hashString
		
```js		
		// md5:
		var params = {data: "Hello World!", hash: "md5"};
		window.hashString(params, function(hash) {
			console.log(params.hash + ": " + hash);
		});
		// sha-256:
		var params = {data: "Hello World!", hash: "sh-256"};
		window.hashString(params, function(hash) {
			console.log(params.hash + ": " + hash);
		});	
```	
	Example File: window.hashFile
```js	
  	var params = {data: "/mnt/sdcard/helloworld.txt", hash: "md5"};
  	window.hashFile(params, function(hash) {
  		console.log(params.hash + ": " + hash);
  	});
```

## Tests:
This has been successfully tested on Phonegap 3.4.0-0.19.11 and Cordova 3.4.0-0.1.3
	
## The MIT License (MIT)

Copyright (c) 2014 Abdsoft

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
