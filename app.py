from flask import Flask, request, render_template
from connect import *
from views.login_handler import *
from views.teleport_handler import *
from views.message_handler import *
import json

def makeApp():
	app = Flask(__name__)
	app.register_blueprint(login_blueprint)
	app.register_blueprint(home_blueprint)
	
	return app

if __name__ == "__main__":
	app = makeApp()
	app.run()