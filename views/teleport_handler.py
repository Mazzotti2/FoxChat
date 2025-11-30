from flask import Blueprint, render_template

home_blueprint = Blueprint("home", __name__, url_prefix="/")

@home_blueprint.route("/")
def homePage():
    return render_template("index.html")

@home_blueprint.route("/login")
def loginPage():
    return render_template("loging.html")

@home_blueprint.route("/register")
def registerPage():
    return render_template("rejestracja.html")

@home_blueprint.route("/chat")
def chatPage():
    return render_template("user_main.html")