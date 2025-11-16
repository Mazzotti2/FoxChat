from flask import Flask, request, render_template
from connect import *
import json

app = Flask(__name__)
id_id = -1

@app.route("/api/login", methods = ["POST"])
def loginHandler():
    username = request.form.get("login")
    password = request.form.get("haslo")

    id_id = login(username, password)

    if id_id > 0:
        response = {
            "status": "success",
            "user_id": id_id,
            "username": username
        }

        return json.dumps(response)
    else:
        response = {
            "status": "failure",
            "message": "Invalid username or password"
        }

        return json.dumps(response)

@app.route("/api/register", methods = ["POST"])
def registerHandler():
    data = request.get_json()
    username = data.get("login")
    password = data.get("haslo")

    if register(username, password):
        id_id = login(username, password)

        if id_id > 0:
            response = {
                "status": "success",
                "user_id": id_id,
                "username": username
            }

            return json.dumps(response)
        else:
            response = {
                "status": "failure",
                "message": "User registration succeeded but login failed"
            }

            return json.dumps(response)
    else:
        response = {
            "status": "failure",
            "message": "Registeration failed"
        }

        return json.dumps(response)

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