$(document).ready(function() {
	$('#select-file').click(function(){
		//sha256_hashfile("/mnt/sdcard/helloworld.txt");
		window.plugins.mfilechooser.open([], function (uri) {
			sha256_hashfile(uri);
		}, function (error) {
			alert(error);
		});
	});
	$('#select-folder').hide();
	$('#select-folder').click(function(){
		//sha256_hashfile("/mnt/sdcard/test.txt");
		
		window.plugins.mfilechooser.open([], function (uri) {
			sha256_hashfile(uri);
		}, function (error) {
			alert(error);
		});
	});
	$('.veryfiy-software').hide();
	
});
var pattern = {
				'B09A2DD3485088D8507B46DFA03D4B3FEC4314B6399F9236B0C17115B14DAB6D':'Tor Browser Bundle v3.6',
				'9E45D97FD2A79435E9B89DC10781AB3F3C12A0F9571904B2F36AE10137A1243D':'GPG4Win v2.2.1',
				'0C3E371A87BE1642FA929B9BCAAB77FE288F68747DCC87EF544B544F3327AB5C':'Thunderbird v24.4',
				'5D371242AF55CAAACE01DDBBB437D5B746C17491DE6F2C989FAC35916582C94C':'TorBirdy add-on for Thunderbird (v0.1.2)',
				'FB39CFA2AF798373F19CD61B6800D880477255031C93A933CAD9F588AFE36E6A':'Enigmail add-on for Thunderbird (v1.6)',
				'BE96534E6AB07395FB4D9B28C6F8E3D482A28CDF5A8DB5801941C3E834FF42E4':'Tor Browser Bundle v3.6 (32-bit)',
				'953546CFEC1D539908148FEACA7142D9F0F9CC18C12C7A6B92197AC81D8CA56D':'Tor Browser Bundle v3.6 (64-bit)',
				'376AB51E3C424DB7E235B2E94494D48CE2FA9A8F1FBF5EF5CF9E367BBAF7422D':'Thunderbird v24.4',
				'AF0EEE8A9EAB91DA3520267D76A449C7945FC3D490449FCC8E6C33C996FEFF13':'Thunderbird v24.4 ',
				'54F98F22D95663144D7C31FA3F1B2690574ABBED9BE6CA1718BE99C9A9C74623':'Tor Browser Bundle v3.6 ',
				'BAEE30F55C50F0DE2E9EFAD826EF1D5D799CFDF1A976E7BCC28BA466D975769D':'Tor Browser Bundle v3.6 ',
				'14921579155B5A834442ABE82DC509CD3627EA220AD9E558FB3C1F45AD43D356':'Tor Browser Bundle v3.6 (32-bit)',
				'86C1E5289E96442F521EBEFD3BD58CBE5963A85679A213FEF7D42D0DFD95BA38':'Tor Browser Bundle v3.6 (64-bit) ',
				'00D8223555DF5B25ED2FAEE2E37787A4726360B92FFF437FA1F032FE65F7210E':'Tor Browser Bundle v3.6 (32-bit)',
				'9967A6337CAF0F3B02C79007B429D7BCC832012055B343F27FE515F8C84DE658':'Tor Browser Bundle v3.6',
				'D738B08A98B535E5537B9546083BB3B1F1D5B3CD60D39126EDA718310ACB4DEA':'Tor Browser Bundle v3.6 (32-bit)',
				'CEFB99CDDCD16D2BD1B197307EB82AD43BB7BB6B1D34A468C98E5CD693224783':'Tor Browser Bundle v3.6 (64-bit)(ar)',
				'91E83C0A29E477530F46A5B6263C224148634AB765EF75B441DD348D14541675':'Tor Browser Bundle v3.6 (32-bit)(ar)',
				'7CEB1E36D523EB358798064641B1FFC837909B88B0AF5FC1DDF9D734129413A6':'Tor Browser Bundle v3.6(zh)',
				'AF61F7EC42313544D4A260EBC815F42BE8C73A30AC80E1B3F298B64F3159E0AF':'Tor Browser Bundle v3.6 (32-bit)(zh)',
				'3A90CBB9625AC5DE5EDED1F3579C53506DDE55E877D3D62815EB9E5261C888ED':'Tor Browser Bundle v3.6 (64-bit)(zh)',
				'6A534765EBA488F6F3E2ACEE9A8F836918EA6B55369A011187B22D7CF59F6034':'Tor Browser Bundle v3.6 (32-bit)',
				'8D25C5B6E3CD6D44C052AD2421D950B1CE71A076B48379368D288A7878279E69':'Tor Browser Bundle v3.6 (32-bit)(de)'
			};

function sha256_hashfile(fileURL){	
	if(fileURL==''){
		return;	//"/mnt/sdcard/helloworld.txt";
	}
	$('.veryfiy-software').show();
	
	var fileNameIndex = fileURL.lastIndexOf("/") + 1;
	var filename = fileURL.substr(fileNameIndex);
	$('.file-name').text(filename);
	
	//var fileURL = "cdvfile://localhost/persistent/Download";
	
	var params = {data: fileURL, hash: "sha-256"};
    window.hashFile(params, function(hash) {
        console.log(params.hash + ": " + hash);
		hashvalue = hash;
		$('.sha-code').text(hashvalue);

        jQuery.getJSON("./data/detector.json", function(data){
            var i=0;
            for(i=0;i<data.length;i++){
                var json=data[i];
                var sha256sum= json.sha256sum;
                var title=json.title;
                //alert("sha256sum:"+sha256sum.toLowerCase()+"hashvalue:"+hashvalue.toLowerCase());
                if(sha256sum.toLowerCase()==hashvalue.toLowerCase()){
                    $('.confirm-software').show();
                    $('#confirm-name').text(title);

                    break ;
                }
                else{
                    $('.confirm-software').hide();
                    //alert("inside else ");
                }
                
            }

        });

		/*if(pattern[hashvalue]){
			$('.confirm-software').show();
			$('#confirm-name').text(pattern[hashvalue]);
		}
		else{
			$('.confirm-software').hide();
		}*/
		
    });
	
}
