console.log('js');

var albumNo=0;
var trackNo=0;
var upAlbums = function upAlbums() {
    console.log('fxn');
    $.get("/update", function(e) {
	console.log('get');
	//div=$('#albums');
	//#console.log(div)
	var info=JSON.parse(e);
	//console.log(info.length);
	albs=document.getElementById('albums');
	var artist=info[albumNo]['artists'];
	//var tracks=JSON.parse(info[albumNo]['tracks']);
	/*albs.innerHTML=tracks;
	albumNo++;
	if (albumNo>5) {
	    albumNo=0;
	    }*/
	//var tracksinfo=info[i]['tracks']
	//for (var i=0;i<5;i++) {
	console.log('ayy');
	//console.log(info[i]['tracks']);
	var allTracks=info[albumNo]['tracks'];
	console.log(info[albumNo]);
	var albumArt=info[albumNo]['image'];
	console.log(albumArt);
	var im=document.getElementById("art");
	console.log('doneim');
	console.log(im);
	im.setAttribute('src', im.getAttribute('src').replace("https://media.giphy.com/media/d2YZa5B3lEAH1soo/giphy.gif", albumArt));



	//im.src=albumArt;
	console.log('setsrc');
	//console.log(im.src);
	//var aImg=document.getElementsByTagName("img");
	//document.getElementById("img").src=albumArt;
	//console.log(aImg);
	//var att=aImg.getAttribute("src");
	//att.value=albumArt;
	//aImg.setAttributeNode(att);
	/*var aImg=document.getElementByID("img");
	console.log(aImg);
	var att=aImg.getAttribute("src");
	att.value=albumArt;
	aImg.setAttributeNode(att);*/

	//document.setAttribute('src', albumArt);

	//aImg.setAttribute('alt', 'na');
	//oImg.setAttribute('height', '1px');
	//oImg.setAttribute('width', '1px');
	//document.getElementById('albumart').innerHTML=aImg;
	//console.log(albumArt);
	var currentTrack=info[albumNo]['tracks'][trackNo];
	console.log('madecurrentrack');
	var currentTrackName=currentTrack['name'];
	console.log('gotname');
	console.log(currentTrackName);
	albs.innerHTML=currentTrackName+'<br>';
	trackNo++;
	if (trackNo==allTracks.length) {
	    trackNo=0;
	    albumNo++;
	}
	console.log(trackNo);
	console.log(albumNo);
	    //console.log(tracksinfo[0]);
	    //console.log(tracksinfo[0]['uri']);
	    //var trackinfo=tracksinfo[0]['uri'];
	    //console.log(artist);
	    //albs.innerHTML=trackinfo+'<br>';;
	    //albs.appendChild(trackinfo+'<br>');
	//};
	
	//albs.innerHTML=info;
	//console.log(info)
    });
};

//upAlbums();
//var interval=setInterval(upAlbums, 3000);
document.getElementById("switch").addEventListener("click", upAlbums);
//document.getElementById("stop").addEventListener("click", function(e) {
    //clearInterval(interval);
//});
