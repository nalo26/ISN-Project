function fill(r, g, b){
	ctx.fillStyle = "rgb("+r+", "+g+", "+b+")";
}
function filla(r, g, b, a){
    a = (100 * a / 255) / 100; //remaping value from [0, 255] to [0, 100] then [0.0, 1.0]
	ctx.fillStyle = "rgba("+r+", "+g+", "+b+", "+a+")";
}

function rect(x, y, w, h){
	ctx.beginPath();
	ctx.rect(x, y, w, h);
	ctx.fill();
	ctx.closePath();
}

function triangle(a, b, c, d, e, f){
	ctx.beginPath();
	ctx.moveTo(a, b);
	ctx.lineTo(c, d);
	ctx.lineTo(e, f);
	ctx.fill();
	ctx.closePath();
}

function image(i, x, y){
	ctx.drawImage(i, x, y);
}

function ellipse(x, y, w, h){
	ctx.beginPath();
	ctx.arc(x, y, w, 0, 2 * Math.PI);
	ctx.fill();
	ctx.closePath();
}

function text(t, x, y){
	ctx.fillText(t, x, y);
}

function textAlign(a){
	ctx.textAlign = ""+a.toLowerCase();
}

function textSize(s){
	ctx.font = s+"px Sans Serif";
}

function random(min, max){
	return Math.floor(Math.random() * (Math.floor(max) - Math.floor(min)) + Math.floor(min));
}

function delay(t) {
	setTimeout(function() {}, t);
}

function background(r, g ,b){
	ctx.fillStyle = "rgb("+r+", "+g+", "+b+")";
	ctx.fillRect(0, 0, canvas.width, canvas.height);
}

function print(t){
	console.log(t);
}

function println(t){
	print(t);
}