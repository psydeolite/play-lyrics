console.log('js');

var albumNo=0;
var upAlbums = function upAlbums() {
    console.log('fxn');
    $.get("/update", function(e) {
	console.log('get');
	div=$('#albums');
	#console.log(div)
	var info=JSON.parse(e);
	console.log(info.length);
	albs=document.getElementById('albums');
	/*var artist=info[albumNo]['artists'];
	var tracks=JSON.parse(info[albumNo]['tracks']);
	albs.innerHTML=tracks;
	albumNo++;
	if (albumNo>5) {
	    albumNo=0;
	    }*/
	//var tracksinfo=info[i]['tracks']
	/*for (var i=0;i<5;i++) {
	    console.log('ayy');
	    var trackinfo=JSON.parse(tracksinfo);
	    //console.log(artist);
	    //albs.innerHTML=artist;
	    //albs.appendChild(artist+'<br>');
	};*/
	
	albs.innerHTML=info;
	console.log(info)
    });
};

//upAlbums();
//interval=setInterval(upAlbums, 3000);
document.getElementById("switch").addEventListener("click", upAlbums);
