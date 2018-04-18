
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

# Strona glowna
@app.route("/")
def route_index():
	return "Test"
	
# Logowanie
@app.route("/login")
def route_login():
	return "Logowanie"

# Rejestracja
@app.route("/register")
def route_register():
	return "Zarejestruj sie juz teraz! Polecam XBot"
	
# Profil uzytkownika
@app.route("/profile/<username>")
def route_profile(username):
	return "Witaj" + username

# Ustawienia profilu
@app.route("/profile/settings")
def route_settings():
	return "Ustawienia"
	
# Follow
@app.route("/profile/<username>/follow")
def route_followe(username):
	return "Wlasnie followujesz uzytkowika: " + username
	
# Cofanie followa
@app.route("/profile/<username>/unfollow")
def route_unfollow(username):
	return "Juz nie followujesz uzytkowika: " + username
	
# Wylogowywanie
@app.route("/logout")
def route_logout():
	return "Wylogowano!"
	
# Errory

	# 404
	@app.errorhandler(404)
	def page_not_found(e):	
		return render_template("templates/404.html"), 404
	

app.secret_key = "dupa"
    