async function validate_register(event) {
	event.preventDefault()
	
	const login = document.getElementById("loginid").value
	const haslo = document.getElementById("hasloid").value
	const haslo2 = document.getElementById("hasloid2").value

	if (haslo == haslo2) {
		//document.getElementById("registerid").submit()
		const res = await fetch("/api/register", {
			method: "POST",
			headers: {"Content-Type":"application/json"},
			credentials: "include",
			body: JSON.stringify({login, haslo})
		})

		const data = await res.json()
	}
	else {
		alert("Hasła nie są identyczne!")
	}
} 