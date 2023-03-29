/** By Ruben Sainders
(c) 15.10.2019 */

document.onload = load_page(true);

function load_page(debug=false){
	// If debug, show message to console
	if (debug == true) {
		console.log("Starting Up...")
	}
	// Hide loader
	document.getElementById("loader").style.display = "none";
}

function On_Click(){
	// Get input
	let num = document.getElementById("number-input").value;
	// Get power
	let power = document.getElementById("power").value;
	let ans = Math.pow(Number(num), Number(power))
	// Output answer
	document.getElementById("answer").innerHTML = "<h3>"+String(answer)+"</h3";
}



