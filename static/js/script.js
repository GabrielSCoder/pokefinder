function randNumber() {
	var num = Math.floor(Math.random() * 903) + 1;
	console.log(num);
	let vl = document.getElementById('rnd');
	vl.value = num;
	var s = document.getElementById('sub');
	s.submit();
}

function darker(){
	var l = document.body
	l.classList.add("bgblack")
}