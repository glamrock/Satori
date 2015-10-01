$(document).ready(function() {
    var bridges = [
					'<input class="getacross" value="194.132.208.14:9968 8311405c99046b6b1628b9628f5f1e3e7daeb398">',
					'<input class="getacross" value="192.36.27.165:28864 8b37facf9449c6e49fb62820bfc307e5bd3a6377">',
					'<input class="getacross" value="77.20.221.213:443 25f931888f0275ebaba65f789b1e2bdd245f3bf3">',
					'<input class="getacross" value="87.122.56.159:443 94bb03a511f2564f70469853a97a4caa1be10675">',
					'<input class="getacross" value="128.78.143.81:443 107406948ff9f08d78cf0449354c5dd0c45ed62b">',
					'<input class="getacross" value="218.146.29.202:443 3dc000f6e2a19add46ba07028dce51df9ce220b2">',
					'<input class="getacross" value="54.84.89.219:443 d4e875fecd0bf023f148871b30d41805999602b4">',
					'<input class="getacross" value="198.23.200.135:443 0a3217df6c520377e627780448c71cfba921e1f2">',
					'<input class="getacross" value="194.132.208.247:29968 9937d1e58cedf0d7f23a0899483b304ef41133d4">',
					'<input class="getacross" value="5.178.64.142:443 8c945a4ee5331662a450d8de8e6c4e162f1871e3">',
					'<input class="getacross" value="192.36.27.30:20195 a6005c8c57b4d2fb63e2795c507676abf8a96314">',
					'<input class="getacross" value="94.34.149.127:9443 54b8748657afa7c94862a495ae1570f78de20cb1">'
				];
    function shuffle(array) {
	  var currentIndex = array.length, temporaryValue, randomIndex;
	  while (0 !== currentIndex) {
		randomIndex = Math.floor(Math.random() * currentIndex);
		currentIndex -= 1;
		temporaryValue = array[currentIndex];
		array[currentIndex] = array[randomIndex];
		array[randomIndex] = temporaryValue;
	  }
	  return array;
	}
	bridges = shuffle(bridges);
	for(randno=0;randno<bridges.length;randno++){		
		 $('.bridge').append(bridges[randno]);
	}
	console.log(bridges);
	
});

