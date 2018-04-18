
from flask import Flask, render_template, request, redirect, session, db

app = Flask(__name__)
db = Database()

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
	return "Witaj: " + username

# Ustawienia profilu
@app.route("/profile/settings")
def route_settings():
	return "Ustawienia"
	
# Follow
@app.route("/profile/<username>/follow")
def route_followe(username):
	if db.is_user(username):
		return "Wlasnie followujesz uzytkowika: " + username
	else:
		return "Brak uzytkownika"
	
# Cofanie followa
@app.route("/profile/<username>/unfollow")
def route_unfollow(username):
	if db.is_user(username):
		return "Juz nie followujesz uzytkowika: " + username
	else:
		return "Brak uzytkownika"
	
	
# Wylogowywanie
@app.route("/logout")
def route_logout():
	return "Wylogowano!"
	
# Errory

# 404
@app.errorhandler(404)
def page_not_found(e):	
	return render_template("404.html"), 404
	

app.secret_key = "dupa"
    