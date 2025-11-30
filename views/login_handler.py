from flask import Blueprint, request
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from connect import *
import json

id_id = -1

login_blueprint = Blueprint("login", __name__, url_prefix="/api")

@login_blueprint.route("/login", methods = ["POST"])
def loginHandler():
    data = request.get_json()
    username = data.get("login")
    password = data.get("haslo")

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

@login_blueprint.route("/register", methods = ["POST"])
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