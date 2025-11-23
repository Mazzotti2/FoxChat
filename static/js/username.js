function get_username() {
	return localStorage.getItem("username")
}

function get_id() {
	return localStorage.getItem("user_id")
}

function hello() {
	const nameBox = document.getElementById("username")
	nameBox.innerText = "user: " + get_username()
}