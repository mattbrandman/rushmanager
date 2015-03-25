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
	reader.readAsDataURL(src);
}

var MAX_HEIGHT = 200;
function render(src, isExternal){
	var image = new Image();
	image.crossOrigin = 'anonymous';
	image.src = src;
	image.onload = function(){
		var canvas = document.getElementById("myCanvas");
		if(image.height > MAX_HEIGHT) {
			//why does this scaling work again (i just want to know the math)
			image.width *= MAX_HEIGHT/image.height;
			image.height = MAX_HEIGHT;
		}
		var ctx = canvas.getContext("2d");
		ctx.clearRect(0, 0, canvas.width, canvas.height);
		canvas.width  = image.width;
		canvas.height = image.height;
		ctx.drawImage(image, 0, 0, image.width, image.height);
		if(isExternal == false) {
			document.getElementById("pictureBase64").value = document.getElementById("myCanvas").toDataURL("image/png")
		}
	};
}