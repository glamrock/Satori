$(document).ready(function() {
	$('#first-log').click(function(){
		window.location.href = 'index.html';
	});	
	$('#page-log').click(function(){
		window.location.href = 'index.html';
	});
	$('#software').click(function(){
		window.location.href = 'software.html';
	});
	$('#guides').click(function(){
		window.location.href = 'guides.html';
	});
	$('#bridges').click(function(){
		window.location.href = 'bridges.html';
	});
	$('#verify').click(function(){
		window.location.href = 'verify.html';
	});
	$('#top-guide').click(function(){
		window.location.href = 'guides.html';
	});
	$('.guide').click(function(){
		window.location.href = 'guides.html';
	});
	$('#page-guide').click(function(){
		window.location.href = 'guides.html';
	});
	$('input').prop('readonly', true);
	//$('input').attr('readonly', true);
	$('a').click(function(){
		assetURL = $(this).attr('href');
		downLoadAsset(assetURL);
		event.preventDefault();
	});
});

function downLoadAsset(urlString){
	alert("Your file is downloading...");
	assetURL = encodeURI(urlString);
	var filename = assetURL.substr(assetURL.lastIndexOf('/')+1);
	
	var targetURL = "cdvfile://localhost/persistent/Download";	
	targetURL = targetURL + '/' + filename;
	
	var ft = new FileTransfer();
	/*ft.onprogress = function(progressEvent) {console.log(progressEvent);console.log('xxx');console.log(progressEvent.lengthComputable);
		alert(progressEvent);alert('xxx');alert(progressEvent.lengthComputable)
		if (progressEvent.lengthComputable) { 
		  //loadingStatus.setPercentage(progressEvent.loaded / progressEvent.total);
		} else {
		  //loadingStatus.increment();
		}
	};
	*/
	
	ft.download(
		assetURL,		
		targetURL,
		function(entry) {
			alert("download complete: " + entry.toURL());
			console.log("download complete: " + entry.toURL());
		},
		function(error) {
			alert("download error source " + error.source);
			console.log("download error source " + error.source);
			console.log("download error target " + error.target);
			console.log("upload error code" + error.code);
		},
		false,
		{
			headers: {
				"Authorization": "Basic dGVzdHVzZXJuYW1lOnRlc3RwYXNzd29yZA=="
			}
		}
	);
	
}