
from flask import Flask

app = Flask(__name__)

@app.route("/")
def route_index():
	return "Test"
    