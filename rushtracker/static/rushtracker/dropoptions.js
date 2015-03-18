var target = document.getElementById("drop-target");
var DTFILE = '';
target.addEventListener("dragover", function(e){e.preventDefault();}, true);
target.addEventListener("drop", function(e){
	e.preventDefault(); 
	avatarPic = e.dataTransfer.files[0];
	loadImage(e.dataTransfer.files[0]);
}, true);
$(document).ready(function(){
	var myform = $('form');
	myform.on('submit', function(e) {
		var testForm = $('form')[0];
		alert(testForm);
		var formdata = new FormData(testForm);
		formdata.append('file', avatarPic);
		e.preventDefault();
		$.ajax({
			url: '/rushtracker/create_rush',
			type: 'POST',
			cache: false,
			contentType: false,
			processData: false,
			data: formdata,

			success:function(data) {
				alert('hi');
			},
		});
	});
});
function loadImage(src){
	//	Prevent any non-image file type from being read.
	if(!src.type.match(/image.*/)){
		console.log("The dropped file is not an image: ", src.type);
		return;
	}

	//	Create our FileReader and run the results through the render function.
	var reader = new FileReader();
	reader.onload = function(e){
		render(e.target.result);
	};
	reader.readAsDataURL(src);
}

var MAX_HEIGHT = 200;
function render(src){
	var image = new Image();
	image.src = src;
	image.onload = function(){
		var canvas = document.getElementById("myCanvas");
		if(image.height > MAX_HEIGHT) {
			image.width  *= MAX_HEIGHT / image.height;
			image.height = MAX_HEIGHT;
		}
		var ctx = canvas.getContext("2d");
		ctx.clearRect(0, 0, canvas.width, canvas.height);
		canvas.width = image.width;
		canvas.height = image.height;
		ctx.drawImage(image, 0, 0, image.width, image.height);
	};
}
