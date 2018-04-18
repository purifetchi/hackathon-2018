
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

@app.route("/")
def route_index():
	return "Test"

app.secret_key = "dupa"
    