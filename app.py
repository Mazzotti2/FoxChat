from flask import Flask, request, render_template
from connect import *

app = Flask(__name__)
id_id = -1

@app.route("/api/login")
def loginHandler():
    username = request.form.get("login")
    password = request.form.get("haslo")

    id_id = login(username, password)

    if id_id > 0:
        return "<script> window.location.href = 'http://127.0.0.1:5500/user_main.html' </script>"
    else:
        return "niezalogowano"

@app.route("/api/register")
def registerHandler():
    data = request.get_json()
    username = data.get("login")
    password = data.get("haslo")

    if register(username, password):
        id_id = login(username, password)

        if id_id > 0:
            return "<script> window.location.href = 'http://127.0.0.1:5500/user_main.html' </script>"
        else:
            return "niezalogowano"
    else:
        return "niezarejestrowano"
    
@app.route("/")
def homePage():
    return render_template("index.html")

@app.route("/login")
def loginPage():
    return render_template("loging.html")

@app.route("/register")
def registerPage():
    return render_template("rejestracja.html")

@app.route("/chat")
def chatPage():
    return render_template("user_main.html")

if __name__ == "__main__":
	app.run()