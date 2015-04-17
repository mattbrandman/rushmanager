$(function() {
	var target = document.getElementById("drop-target");
	target.addEventListener("dragover", function(e){e.preventDefault();}, true);
	target.addEventListener("drop", function(e){
		e.preventDefault(); 
		loadImage(e.dataTransfer.files[0]);
	}, true);
})
function loadImage(src){
	//	Prevent any non-image file type from being read.
	
	if(!src.type.match(/image.*/)){
		console.log("The dropped file is not an image: ", src.type);
		return;
	}

	//	Create our FileReader and run the results through the render function.
	var reader = new FileReader();
	reader.onload = function(e){
		render(e.target.result, false);
	};
	reader.onloadend = function() {
		document.getElementById('id_pic64Value').value = reader.result;
	}
	reader.readAsDataURL(src);
}
//maybe I should scale down until I hit a certain height?
var MAX_HEIGHT = 300;
function render(src, isExternal){
	var image = new Image();
	image.crossOrigin = 'anonymous';
	image.src = src;
	image.onload = function(){
		var canvas = document.getElementById("myCanvas");
		var ctx = canvas.getContext("2d");
		canvas.width  = 300;
		canvas.height = 300;
		if (image.width-image.height > 50) {
			ctx.drawImage(image, 0, 0, canvas.width, canvas.height);
		} else {
			ctx.drawImage(image, 0, 0, canvas.width, image.height);
		}	
	};
}