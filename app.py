
from flask import Flask, render_template, request, redirect, session
from db import Database
import json

app = Flask(__name__)
db = Database()

# Strona glowna
@app.route("/")
def route_index():
	if 'username' in session:
		info = db.get_user_info(session['username'])
		following = json.loads(info["follows"])
		print(following)
	else:
		following = None
	return render_template("index.html", following=following, db=db)
	
# Logowanie
@app.route("/login", methods=['GET', 'POST'])
def route_login():
	if request.method == 'POST':
		if db.auth_user(request.form["username"], request.form["passwd"]):
			session["username"] = request.form["username"]
			return redirect("/", code=302)
		else:
			return redirect("/login", code=302)
	else:
		return render_template("login.html")

# Rejestracja
@app.route("/register", methods=['GET', 'POST'])
def route_register():
	if request.method == 'POST':
		if db.register_user(request.form["username"], request.form["passwd"]):
			session["username"] = request.form["username"]
			return redirect("/", code=302)
		else:
			return redirect("/register", code=302)
	else:
		return render_template("register.html")
	
# Profil uzytkownika
@app.route("/profile/<username>")
def route_profile(username):
	if db.is_user(username):
		userinfo = db.get_user_info(username)
		if 'username' in session:
			following = db.get_user_info(session["username"])["follows"]
		else:
			following = ""
		posts = db.get_user_posts(username)
		return render_template("profile.html", info=userinfo, posts=posts, following=following)
	else:
		return "Brak uzytkownika"

# Wysyłanie wpisów
@app.route("/post", methods=['POST'])
def route_post():
	if "username" in session:
		if db.add_post(session['username'], request.form["post"]):
			return redirect("/profile/" + session['username'], code=302)

# Ustawienia profilu
@app.route("/profile/settings", methods=['GET', 'POST'])
def route_settings():
	if request.method == 'POST':
		if 'username' in session:
			db.update_data(session['username'], request.form["passwd"], request.form["avatar"])
			return redirect("/profile/" + session['username'], code=302)
	else:
		if "username" in session:
			user_info = db.get_user_info(session['username'])
			return render_template("settings.html", avatar=user_info['avatar'])
		else:
			return "Najpierw sie zaloguj"
	
# Follow
@app.route("/profile/<username>/follow")
def route_followe(username):
	if db.is_user(username) and 'username' in session:
		db.follow_user(session['username'], username)
		return redirect("/profile/" + username, code=302)
	else:
		return "Brak uzytkownika"
	
# Cofanie followa
@app.route("/profile/<username>/unfollow")
def route_unfollow(username):
	if db.is_user(username) and 'username' in session:
		db.unfollow_user(session['username'], username)
		return redirect("/profile/" + username, code=302)
	else:
		return "Brak uzytkownika"
	
	
# Wylogowywanie
@app.route("/logout")
def route_logout():
	session.clear()
	return redirect("/", code=302)
	 
# Errory

# 404
@app.errorhandler(404)
def page_not_found(e):	
	return render_template("404.html"), 404

# 505
@app.errorhandler(500)
def page_not_found(e):	
	return render_template("500.html"), 500
	
	


app.secret_key = "dupa"
    