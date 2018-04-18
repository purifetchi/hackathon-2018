
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

// Strona glowna
@app.route("/")
def route_index():
	return "Test"
	
// Profil uzytkownika
@app_route("/profile/<username>")
def route_profile(username)
	return "Witaj" + username

app.secret_key = "dupa"
    