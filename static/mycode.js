console.log('js');

var albumNo=0;
var trackNo=0;
var upAlbums = function upAlbums() {
    console.log('upAlbums');
    //console.log(document.getElementById('search'));
    console.log('SOMETHING');
    $.get("/update", function(e) {
	console.log('update');
	var info=JSON.parse(e);
	$('#albumInfo').text('');
	
	var artist=info[albumNo]['artists'];
	var allTracks=info[albumNo]['tracks'];
	var albumArt=info[albumNo]['image'];
		
	$('#art').attr('src', albumArt);
	
	var currentAlbum=info[albumNo]['name'];
	var currentTrack=info[albumNo]['tracks'][trackNo];
	var currentTrackName=currentTrack['name'];
	var currentArtistName=currentTrack['artists'];
	var currentURI=currentTrack['uri'];

	var toInsert='Album: '+currentAlbum+'<br>Artist: '+currentArtistName+'<br>Song: '+currentTrackName+'<br>';
	//$('#albumInfo').text(currentTrackName+' by '+currentArtistName+' on '+currentAlbum);
	$('#albumInfo').text('Album: '+currentAlbum);
	$('#albumInfo').append('<br>');
	$('#albumInfo').append('Artist: '+currentArtistName);
	$('#albumInfo').append('<br>');
	$('#albumInfo').append('Song: '+currentTrackName);
	$('#albumInfo').append('<br>');
	//s1='<iframe src="https://embed.spotify.com/?uri='
	//s2=' width="300" height="380" frameborder="0" allowtransparency="true"></iframe>'
	//compl=s1+currentURI+s2;
	//console.log(compl);
	//$('body').append(compl);
	trackNo++;
	if (trackNo==allTracks.length) {
	    trackNo=0;
	    albumNo++;
	}
	
    });
};

//document.getElementById("switch").addEventListener("click", upAlbums);

var getLyrics=function getLyrics() {
    console.log('getLyrics');
    var searchKey=$('#searchKey').val();
    console.log(searchKey);
    var url = '/search?searchKey='+searchKey;
    $('#lyrics').text('Loading lyrics...');
    $.get(url, function(e) {
	console.log('search');
	
	var info=JSON.parse(e);
	console.log(info);
	$('#lyrics').text('');
	var lyricLines=info.split('\n');
	//var loc=info.indexOf('\n');
	console.log(lyricLines);
	for (var i=0; i<lyricLines.length; i++) {
	    if (i!==lyricLines.length-1) {
		$('#lyrics').append(lyricLines[i]);
		$('#lyrics').append('<br>');
	    }
	};
	
    });
};

document.getElementById("search").addEventListener("click", getLyrics);

upAlbums();
interval=setInterval(upAlbums, 1000);


//document.getElementById("stop").addEventListener("click", function(e) {
//    clearInterval(interval);
//});
